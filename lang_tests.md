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
qPart = `[?customer 5 ?fullName .]`
kinds = [list of unique kinds in query part]
wrapper = database wrapper for this query part

for kind in kinds:
    wrapper.addKind(kind)

for statement in qPart:
    if statement is a triple:
        subject, morphism, object = statement
        kind, mapping = getKind(morphism)
        propertyName = getPropertyName(morphism, mapping)
        if isRootProperty(morphism, mapping):
            wrapper.addSelection(kind, propertyName)  # We don't have to worry about cardinality with just one morphism like this

return wrapper.buildQuery()
```

```
SELECT full_name
FROM customer
```


### A02 Trivial selection from single kind (dual morphism)

```
SELECT {
    ?customer fullName ?fullName .
}
WHERE {
    ?customer -95 ?fullName . # Dual morphism of 95, which is dual morphism of 5, meaning this should mean 5
}
```

TODO: solution

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

TODO: solution

### A04 Selection from two kinds using path notation (JOIN)

```
SELECT {
    ?order id           ?orderId      ;
           customerName ?customerName .
}
WHERE {
    ?order 14/4 ?customerName ;
        13 ?orderId .
    ?customer 4 ?customerName .
}
```

TODO: solution

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

TODO: solution

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
