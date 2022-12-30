# Querycat Language Tests

First point - how do we interpret SELECT clause? Do we return a single graph with many entries, or do we return multiple?
Like multiple instance categories with one category for each "solution"?

## Relational queries (SQL)

### Simple query

```sql
SELECT name, price
FROM items
WHERE price <= 150
```

```
SELECT {
  ?item name  ?itemName  ;
        price ?itemPrice .
}
WHERE {
  ?item 56 ?itemName ;
        57 ?itemPrice .
  FILTER (?itemPrice <= 150)
}
```

### Joins

```sql
SELECT items.name, items.price, reviews.rating
FROM items INNER JOIN reviews ON items.id = reviews.item_id
```

```
SELECT {
  ?item name  ?itemName  ;
        price ?itemPrice ;
        rating ?itemRating .
}
WHERE {
  ?item 56 ?itemName ;
        57 ?itemPrice ;
        -40 ?review .

  ?review 42 ?itemRating .
}
```

### Max / Min / Count + Order By

```sql
SELECT item_id, AVG(rating) as avgRating
FROM reviews
ORDER BY avgRating DESC

```

```
SELECT {
    ?item averageRating AVG(?rating) AS ?avg .
}
WHERE {
    ?review 40 ?item ;
            42 ?rating .
}
ORDER BY ?avg
```

or we can do `AVG(?rating) as ?avgRating` in the SELECT also? But then how does the order by semantics work?

Does that make sense? I see it as "order the solutions matched by WHERE, and pass them in that order to SELECT".
But if we return 1 graph then this does not make sense actually.
This also concerns `LIMIT` and `OFFSET`!

-> we create a 2nd graph denoting the order of connected components, ORDER BY and LIMIT operate on these connected components

### Subquery (items with maximal average rating from all items in database)

```sql
SELECT item_id, AVG(rating) AS avgRating
FROM reviews
GROUP BY item_id
HAVING avgRating = (
    SELECT MAX(itemAvgRating)
    FROM (
        SELECT item_id, AVG(rating) AS itemAvgRating
        FROM reviews
        GROUP BY item_id
    )
)
```

```
SELECT {
    ?item avgRating ?maxRating .
}
WHERE {
    # Subselect would work as binding the graph from SELECT into the same context as WHERE
    # So in this case we only have 1 node with the max rating
    {
        SELECT {
            MAX(?itemAvgRating) as ?maxRating .
        }
        WHERE {
            {
                SELECT {
                    ?itemWithAvg avgRating AVG(?itemRating) AS ?itemAvgRating .
                }
                WHERE {
                    ?itemWithAvg 42 ?itemRating .
                }
            }
        }
    }
    ?item rating ?itemRating .

    FILTER (AVG(?itemRating) == ?maxRating)
}
```

### Group By

Does it make sense for us to introduce Group By?

-> provest diskusi: group by je tam implicitne, priklady

## Document oriented (MongoDB)

### Arrays

TODO: how do we represent arrays from MongoDB in the schema category?

    _Pole nad strukturovanym dokumentem_:
    Order <- Items -> _ -> Name
                        -> Price
              \/
              Key (v tom pripade to je key/value dict, nebo misto Key je Index a pak to je pole)
    
    _ je anonymni jeden produkt z pole

    _Pole nad primitivni hodnotou_:
    Person <- Names -> Name

### Arrays of embedded documents

see above

## Graph oriented

We have a graph oriented language already, so we support everything needed.



-> kouknout na multimodel benchmark, prevzit nejake dotazy a na nich to ukazat, jak se to mapuje do tech databazi atd
https://github.com/HY-UDBMS/UniBench


V1:
```
SELECT {
    _:friendsOrders friend ?friendA ;
                    friend ?friendB ;
                    numCommonProducts COUNT(?commonProduct) AS ?numCommonProducts .
}
WHERE {
    ?friendA 100/200 ?friendB .
    # Eliminate duplicate pairs of friends with swapped order
    FILTER(?friendA < ?friendB)

    ?friendA -21/23/-36/-39 ?commonProduct .
    ?friendB -21/23/-36/-39 ?commonProduct .
}
ORDER BY ?numCommonProducts DESC
```

V2:
```
SELECT {
  _:friendsOrders friend ?friendA ;
                  friend ?friendB ;
                  numProds COUNT(DISTINCT ?comProd) AS ?numProds .
    ?friendA name ?friendAName ;
             surname ?friendASurname .
    ?friendB name ?friendBName ;
             surname ?friendBSurname .         
}
WHERE {
    ?friendA 100/200 ?friendB .
    FILTER(?friendA < ?friendB)

    ?friendA -21/23/-36/-39 ?comProd ;
             3 ?friendAName ;
             7 ?friendASurname .
    ?friendB -21/23/-36/-39 ?comProd ;
             3 ?friendBName ;
             7 ?friendBSurname .
}
ORDER BY ?numCommonProducts DESC
```

# Translating queries

TODO: do we consider root morphisms?

- Basic input from query parsing = set of triples in the `WHERE`, set of triples in `SELECT`
    - Plus other constraints (`FILTER`, `ORDER BY`, subqueries, ...)

1. Identify which kinds are queried
    - Each triple references a morphism.
    - This morphism may be looked up in the mappings - sometimes there is rendundancy -> select all matching kinds
    - We need to use `ids` property of schema objects to figure out how they are connected
    - TODO: how do we deal with inlining? We need to correctly use inlined properties like `customer_id` etc.
        Also can we let users query inlined properties? It may be disjointed in the schema category (or can it?)
2. Generate query plans and choose a query plan (if not already chosen)
    - Choosing a query plan may involve asking database wrappers about performance of a query
        -> Each DB wrapper has a method to either query a set of kinds, or to evaluate the performance of that query
    - After a query plan is chosen, we can assume an unambiguous "global access path" over all kinds to be the base of the query
    - Every morphism in a query must be contained in a mapping
        -> joining does not happen on morphisms, but on vertices
3. For each queried kind, identify which fields are queried, and ignore other ones in further processing
    - Basically create a subtree from the access path of every kind's mapping
    - We must correctly also query things like `ids` from other kinds
4. Call database wrappers, giving each a list of kinds to query
    - Here we also specify other parameters like `FILTER`s etc
    - These kinds must be contiguous in the schema category (so they can be joined)
    - TODO: how about queries which reference a kind multiple times?
    -> We have an instance category, and results of query parts (or kinds) are added to the same instance category.
        Then we are finished because the same data is in both instance categories being joined. (-> merge join)
5. Each database wrapper will return a set of instances (schema implied by the kinds queried)
    - Each instance is rooted in the root of one of the kinds since the mappings given to the wrappers must form a DAG (TODO: verify)
    - For ordering, a DB wrapper returns another instance which induces ordering between the returned instances
6. Do the necessary ad-hoc joins between instances
    - We must take the instances returned by DB wrappers and merge them to create instances matching "all data returned by `WHERE`"
7. Do projection on these instance categories to create results and return them

https://www.ksi.mff.cuni.cz/~koupil/images/05-postgresql-orders-1.png
https://www.ksi.mff.cuni.cz/~koupil/images/06-postgresql-orders-2.png

Todo do diplomly: seznam optimalizaci o kterych vime ale zatim jsme neresili
    - vicekrat vyskyt morfismu v dotazu -> deduplikace
    - open question: optimalizace poradi joinovani vysledku query parts
    - benchmarking: vytvorit jen dummy rozhrani a pak do diplomky napsat ze to je future work

Planner provede dekompozici na query parts
-> Pro kazdou query part:
    - inicializuje si wrapper pro query part
    - prochazi query part (schematicka kategorie + mapping), postupne na wrapperu vola ruzne metody (projekce, selekce, join, atd.)
    - wrapper vi jestli podporuje urcite koncepty, a pokud ano tak jakym zpusobem je podporuje (wrapper si to sam nejak implementuje)
    - nakonec se zavola na wrapperu neco jako createDDLstatement() (Algorithm 4: DDL Algorithm)
    - abstraktni terminologie: link na prezentaci
    - hlavni prinos prace = univerzalni algoritmy na preklad query parts

Do diplomky: use cases - proof of concept, nejaky konkretni data a dotazy, muzu pouzit multimodel dotaz atd
Na demo: dodelat frontend (screenshot) + par vet o technologiich, deploy to github pages
First steps: napsat si pseudokod obecneho algoritmu na preklad dotazu na papir, udelat si ~10-12 dotazu a odladit si to na papire
Do diplomky: klidne muzu dat "naivni" algoritmus, a pak dat lepsi verze
(na overleafu inspirace papers pro psani, algoritmy tabulky atd)


# Unit tests

!!! Trivial algorithm = process `WHERE` clause, get results, and only then care about `SELECT`
    -> this leads to inefficiencies with aggregation etc, but we can optimize it with a better algorithm
       which takes into account what is needed in the `SELECT` clause
    -> naive algorithm could only support some construct (not all), but we can extend it with more naive algorithms
       and the final algorithm can have all features

what do we do with `FROM` clause in MMQL?
    -> I think we can use it to select schema category + mappings if we have multiple sets

can create a table with each unit test + created queries in given languages -> look for similarities (determines if we need nesting)

When doing selection/joining between kinds (traversing any morphism), we have to tell the wrapper in which direction we are traversing
the morphism (either that or max cardinality) -> we assume that unlisted dual morphisms have max cardinality *.
If we pass this to the wrapper, the wrapper can decide for example if it should use left or right join.
In the simplest version of the algorithm, we can skip this part and the wrapper will have to do full outer join
every time, which will return tons of data but it still works.

## Section A - Some simple kinds with a join table (all PostgreSQL)

Mappings of kinds:
```
customer: {
    id: 4,
    full_name: 5
}
order: {
    id: 13,
    delivery_address: 12,
    note: 11,
    created: 8,
    sent: 9,
    paid: 10,
    customer_id: 4.14
}
order_item: {
    order_id: 13.21,
    product_id: 15.20,
    amount: 19,
    total_price: 18
}
product: {
    id: 15,
    name: 16,
    price: 17
}
```

### A01 Trivial selection from single kind

```
SELECT {
    ?customer fullName ?fullName .
}
WHERE {
    ?customer 5 ?fullName .
}
```

```
qPart = `[?customer 5 ?fullName]`
kinds = [list of unique kinds in query part]
wrapper = database wrapper for this query part

for kind in kinds:
    wrapper.addKind(kind)

for statement in qPart:
    if statement is a triple:
        subject, morphism, object = statement
        kind, mapping = getKind(morphism)
        if isRootProperty(morphism, mapping):
            propertyName = getPropertyName(morphism, mapping)
            wrapper.addProjection(kind, propertyName, isDual=False)

return wrapper.buildQuery()
```

```
SELECT id, full_name
FROM customer
```

```
db.customer.aggregate([
    { $project: { full_name: 1 } }
])
```

-> returns:
```
1, Adam Atkinson
2, Beatrice Betwixt
3, Chester Camelot
4, Daniel Dastardly
```

-> instance category:
customer (instance object):
    {(id, 1)}
    {(id, 2)}
    {(id, 3)}
    {(id, 4)}

full name (instance object):
    {(ε, "Adam Atkinson")}
    {(ε, "Beatrice Betwixt")}
    {(ε, "Chester Camelot")}
    {(ε, "Daniel Dastardly")}

5 (instance morphism):
    ((id, 1), (ε, "Adam Atkinson"))
    ((id, 2), (ε, "Beatrice Betwixt"))
    ((id, 3), (ε, "Chester Camelot"))
    ((id, 4), (ε, "Daniel Dastardly"))

Instantiation of `SELECT` clause:
    for each variable in `SELECT`:
        include the active domain of that variable in the result instance category

    for each triple in `SELECT`:
        subject, morphism, object = triple
        instance morphism = compound instance morphism between subject and object in the instance category


#### A01b The same but with MongoDB

### A02 Trivial selection from single kind (dual morphism)

```
SELECT {
    ?customer fullName ?fullName .
}
WHERE {
    ?fullName -5 ?customer .
}
```

```
qPart = `[?fullName -5 ?customer]`
kinds = [list of unique kinds in query part]
wrapper = database wrapper for this query part

for kind in kinds:
    wrapper.addKind(kind)

for statement in qPart:
    if statement is a triple:
        subject, morphism, object = statement
        if isDual(morphism):
            kind, mapping = getKind(dual(morphism))
        else:
            kind, mapping = getKind(morphism)
        if isRootProperty(dual(morphism), mapping):
            propertyName = getPropertyName(dual(morphism), mapping)
            wrapper.addProjection(kind, propertyName, isDual=isDual(morphism))

return wrapper.buildQuery()
```

The query and instance category here should be the same as in A01.

### A03 Selection from two kinds with explicit variable (JOIN)

```
SELECT {
    ?order id           ?orderId      ;
           customerName ?customerName .
}
WHERE {
    ?order 14 ?customer ;
        13 ?orderId .
    ?customer 4 ?customerName .
}
```

```
qPart = `[?order 14 ?customer, ?order 13 ?orderId, ?customer 4 ?customerName]`
kinds = [list of unique kinds in query part]
wrapper = database wrapper for this query part

for kind in kinds:
    wrapper.addKind(kind)

for statement in qPart:
    if statement is a triple:
        subject, morphism, object = statement
        kind, mapping = getKind(morphism)
        if isRootProperty(morphism, mapping):
            propertyName = getPropertyName(morphism, mapping)
            if isInlinedFromAnotherKind(morphism, mapping):
                if is part of `ids` in that kind: # TODO: what if it's not?
                    wrapper.addProjection(kind, propertyName)
                    otherKind = getOtherKind(kind, morphism) # TODO: what if there are multiple kinds like this? what then?
                    otherPropertyName = getPropertyName(last base morphism of inlined morphism, otherKind.mapping)
                    wrapper.addJoin(kind, otherKind, propertyName, otherPropertyName)
            else:
                wrapper.addProjection(kind, propertyName)

return wrapper.buildQuery()
```

```
SELECT order.id, order.customer_id, customer.full_name # TODO: IMO we do need the customer ID in the instance category
FROM order INNER JOIN customer ON order.customer_id = customer.id
```

Instantiation of `SELECT` clause:
    for each variable in `SELECT`:
        include the active domain of that variable in the result instance category

    for each triple in `SELECT`:
        subject, morphism, object = triple
        instance morphism = compound instance morphism between subject and object in the instance category

### A04 Selection from two kinds using path notation (JOIN)

```
SELECT {
    ?order id           ?orderId      ;
           customerName ?customerName .
}
WHERE {
    ?order 14/4 ?customerName ;
        13 ?orderId .
}
```

Compound morphisms like this are processed by the trivial algorithm identically to case A03,
meaning the `14/4` shorthand is treated as if a variable was manually specified for each composition.
The improved algorithm versions can skip selecting intermediate data, and already include a composite
instance morphism in the instance category induced by the `WHERE` clause.

### A05 Selection from one kind using FILTER

```
SELECT {
    ?customer name ?customerName .
}
WHERE {
    ?customer 4 ?customerName ;
        3 ?customerId .
    
    FILTER(?customerId == 42)
}
```

```
qPart = `[?customer 4 ?customerName, ?customer 3 ?customerId, FILTER(?customerId == 42)]`
kinds = [list of unique kinds in query part]
wrapper = database wrapper for this query part

for kind in kinds:
    wrapper.addKind(kind)

for statement in qPart:
    if statement is a triple:
        subject, morphism, object = statement
        kind, mapping = getKind(morphism)
        if isRootProperty(morphism, mapping):
            propertyName = getPropertyName(morphism, mapping)
            wrapper.addProjection(kind, propertyName, isDual=False)
    else if statement is `FILTER`:
        lhs, operator, rhs = statement
        if lhs is variable and rhs is constant:
            if lhs is root property of kind:
                propertyName = property name of lhs in kind
                wrapper.addSelection(kind, propertyName, condition={
                    operator: operator,
                    constant: rhs,
                })

return wrapper.buildQuery()
```

```
SELECT id, full_name
FROM customer
WHERE id = 42
```

### A06 Selection using join table

```
SELECT {
    ?order id ?orderId ;
        contains ?name .
}
WHERE {
    ?order -21/20 ?product ;
        13 ?orderId .
    ?product 16 ?name .
}
```

TODO: solution

### A07 Selection using join table (using long path to test cardinalities)

```
SELECT {
    ?order id ?orderId ;
        contains ?name .
}
WHERE {
    ?order -21/20/16 ?name ;
        13 ?orderId .
}
```

TODO: solution

### A08 Optional matching

```
SELECT {
    ?customer id ?customerId ;
        hasOrderId ?orderId .
}
WHERE {
    ?customer 4 ?customerId .
    OPTIONAL {
        ?customer -14/13 ?orderId .
    }
}
```

TODO: solution

### A09 Optional matching with COUNT aggregation

```
SELECT {
    ?customer id ?customerId ;
        numOrders COUNT(?orderId) AS ?numOrders .
}
WHERE {
    ?customer 4 ?customerId .
    OPTIONAL {
        ?customer -14/13 ?orderId .
    }
}
```

TODO: solution

### A10 Optional matching with filtering on COUNT aggregation

```
SELECT {
    ?customer id ?customerId ;
        numOrders COUNT(?orderId) AS ?numOrders .
}
WHERE {
    ?customer 4 ?customerId .
    OPTIONAL {
        ?customer -14/13 ?orderId .
    }
    
    FILTER (COUNT(?orderId) >= 10)
}
```

# Algorithm

// TODO: morphism cardinality meaning -> what does it mean?
    - it always is 0,1 lower, 1 upper
// TODO: traversing morphisms with minus -> we always do inner join anyways? why does it matter?
    - technically it can be just inner join, but maybe left/right join is faster? -> evaluate, try to maybe find a paper about it

## Creating query plan

For each morphism in query `WHERE` clause:
    If morphism is only in one kind:
        Assign morphism to that kind
    Else morphism is in multiple kinds:
        Create query plans for all possibilities

-> only allow selecting from morphisms which have their root in the `WHERE` clause
    -> otherwise we can e.g. try to select all products from orders collection in mongo (can be incomplete, duplicities)

// TODO: do we need to prune invalid plans? Like could not using the whole inlined morphism be invalid?

Query plan = list of morphisms, each has a source kind assigned, maximal contiguous subgraphs from the same DB are called query parts
    -> example of non contiguous: customers and orders in postgre, but not between them
    -> not distinct - recursion (we try to do the whole recursion in the system at the same time if it supports it)
    -> transitivity vs repeated query parts (+ create example for each case)

-> constraint of our approach: we only consider explicit statements, not user defined functions

## Creating join plans for each query plan

For each pair of neighboring query parts:
    Find intersection schema object (always exists, can be multiple if multiple identifiers)
    Define instance category join in this schema object (always inner join)
    For both query parts, add selection of `ids` properties of the intersection schema object

For each query part:
    // TODO: determine reasons that it cannot be satisfied (e.g. no support for joins and multiple kinds)
    // TODO: merge graph traversal and join capability into just join capability
    If query part cannot be satisfied by 1 query:
        Split query part into multiple so that each can be satisfied with 1 query
        For each cross-cutting statement for this query part:
            Add this statement to list of things to execute manually

## Selecting the best query plan

// TODO: for now we can select for example the lowest number of joins
// Penalize inefficient query plans based on heuristics
For each query plan:
    // (mongo)-(postgre)-(mongo) vs (mongo)-(mongo)-(mongo)
    If plan contains jagged paths then penalize plan
    If plan contains aggregations which cannot be done on DB level then penalize plan
    If plan involves a lot of joining on engine level then penalize plan
    If limit/orderby/skip/aggregations have to be done on engine level then penalize plan

## Processing query parts

(So far this does not consider `ORDER BY` and `LIMIT/OFFSET`, as well as projection-level
aggregations and subqueries)

Create DB wrapper for this query part
For each variable in query part:
    // For example 2 different customer variables have separate mappings because we want to use different operations on them
    Define variable-kind mapping in wrapper

For each statement in query part:
    If statement is a triple with a composite morphism:
        Decompose triple into separate triples with base morphisms // TODO: can we do this? For example how about inlined attributes and their selection

For each statement in query part:
    If statement is a triple:
        subject, predicate, object = statement
        if subject or object is in another query part:
            defer selection to merging step
        if subject and object are within the same kind:
            if subject and object are nonterminals:
                do nothing
            else if subject is nonterminal and object is terminal:
                if subject is root:
                    // TODO: add solution for 2 different subjects leading to the same variable in two triples (selection? how?)
                    wrapper.addProjection(getKind(subject), property)
                else:
                    // TODO: do we actually need two different methods? I think we don't, and the same in selection
                    wrapper.addNestedProjection(getKind(subject), property)
            else if subject is terminal and object is nonterminal:
                do the same as the other way around, just for subject
        else subject and objects are in different kinds from this query part:
            one of these kinds has some kind of inlined property from the other kind // TODO: is this always true? how about graph models? And how about cases when there are multiple in common?
            find the inlined property (the morphism is part of it)
            if wrapper.supportsGraphTraversal:
                wrapper.addTraversal(getKind(subject), getKind(object))
            else if wrapper.supportsJoins:
                // TODO: I don't think we need any extra projection here
                wrapper.addJoin(getKind(subject), getKind(object), commonPropertyBetweenKinds)

    Else if statement is `FILTER`:
        lhs, operator, rhs = statement
        if lhs > rhs then swap lhs and rhs // Ordering given variable > aggregation > constatnt
        if lhs is variable and rhs is constant:
            wrapper.addSelection(getKind(lhs), getPropertyName(lhs), condition={
                operator: operator,
                constant: rhs,
            })
        else if lhs is variable and rhs is variable:
            if lhs and rhs are in this query part:
                wrapper.addSelection(getKind(lhs), getPropertyName(lhs), getKind(rhs),
                    getPropertyName(rhs), operator)
            else:
                defer selection to merging step
        else if lhs is variable and rhs is aggregation:
            if lhs and rhs variable are in this query part:
                wrapper.addAggregation(getKind(rhs), aggregationKind(rhs), alias)
                wrapper.addSelection(getKind(lhs), getPropertyName(lhs), alias, operator)
            else:
                defer selection to merging step
        else:
            // TODO: does it make sense to support cases with 2 aggregations or 1 aggregation and 1 constant?
    Else if statement is `OPTIONAL`:
        ...
    Else if statement is `UNION`:
        ...
    // TODO: are we going to have `INTERSECTION`? SPARQL doesn't have it
        -> we don't need the clause in MMQL, as for generating queries then we can use joins+selection for now, but it is more efficient to generate intersection
    Else if statement is `MINUS`:
        ...
    Else:
        Not supported

// TODO: should the DB wrapper itself do joins if multiple queries? Or should the algorithm create multiple wrappers and join results?
// My proposed solution is to use the wrapper to divide the query into parts where each can be satisfied with 1 query
// Then we join them and execute any possible remaining filters manually
Build query from wrapper
Execute query and receive instance category from wrapper
Return given instance category

## Merging query parts

Get list of instance categories from list of query parts (1 per each)
For each join in list of joins:
    Join instance categories using the join condition, creating a merged instance category

For each delayed statement:
    Execute delayed statement

Result of this step is an instance category representing the `WHERE` clause, with bindings for each variable

// TODO: we can't do merging with evocat for now because we can't get the data/statements into it

## Projection

-> zakazeme kruznice v `WHERE` klauzuli (s vyjimkou rekurze)

for each variable in `SELECT`:
        include the active domain of that variable in the result instance category

for each triple in `SELECT`:
    subject, morphism, object = triple
    if object is constant:
        instance morphism = morphism projecting to the constant
    else if object is variable:
        instance morphism = compound instance morphism between subject and object in the instance category
    else if object is aggregation:
        calculate compound morphism between subject and object, and use it to calculate the aggregation
        instance morphism = morphism projecting to the aggregation result
    
    if object is an alias:
        add variable to list of aliases

if query has `ORDER BY`, `LIMIT` or `OFFSET`:
    introduce additional ordering instance category
    if limit or offset is present, implement by counting nontrivial connectivity components in the instance category

return finished instance category