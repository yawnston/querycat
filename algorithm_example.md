// Vsechny pristupove cesty jsou validni pro nejaky model a naopak -> nemusime v algoritmu resit explicitne nejak grafovy model, staci rict ze umime pristupove cesty a tim umime vsechno

# Algorithm example

```
SELECT {
    ?order id ?orderId ;
        customerName ?customerName .
}
WHERE {
    ?order 10 ?orderId ;
        9/2 ?customerName .
}
```

## 1. Create query plans

For morphism in [10,9/2]:
    Split morphism into base morphisms with temporary variables

// This does not yet consider recursive/repeating query parts
For morphism in [10,9,2]:
    For each kind where morphism is:
        Add mapping (morphism, kind) to query plan

Result: {
    10: [Order<MongoDB>],
    9: [Order<MongoDB>],
    2: [Customer<PostgreSQL>,Customer<MongoDB>]
}

Generate all possible combinations of morphism-kind assignments to get query plans

Query plans: [
    {
        id: 1,
        10: [Order<MongoDB>],
        9: [Order<MongoDB>],
        2: [Customer<PostgreSQL>]
    },
    {
        id: 2,
        10: [Order<MongoDB>],
        9: [Order<MongoDB>],
        2: [Customer<MongoDB>]
    }
]

Traverse each query plan starting with random node
For node in traversal:
    If getDatabase(node) != getDatabase(prevNode):
        Split query parts here
    Else if not getWrapper(node).supportsJoin:
        Split query parts here

Query plans: [
    {
        id: 1,
        {
            id: A,
            10: [Order<MongoDB>],
            9: [Order<MongoDB>],
        },
        {
            id: B,
            2: [Customer<PostgreSQL>]
        }
    },
    {
        id: 2,
        {
            id: C,
            10: [Order<MongoDB>],
            9: [Order<MongoDB>],
            2: [Customer<MongoDB>]
        }
    }
]

## 2. Create join plans

The join plan for query plan #2 is trivial, so let's examine the one for #1:

For each pair of neighboring query parts:
    Match the pattern (objA) -m-> (objB)
    kindA = kind(objA), kindB = kind(objB)
    For id in ids(objB):
        If all properties of id can be selected from kindA:
            Add join plan for queryPart(kindA), queryPart(kindB) on id
            Add projection of id to kindA, 
            // Constraint = only joining on keys, not on arbitrary attributes -> explain in thesis

Join plan: [
    {
        queryPartA: A,
        queryPartB: B,
        id: {1}
    }
]

## 3. Select the best query plan

Let us assume that we picked plan #1 for showcase, otherwise plan #2 is probably best

## 4. Processing query parts

queryPartA: {
    ?order 10 ?orderId .
    ?order 9 ?customer .
    ?customer 1 ?customerId .
}
    - wrapper.addProjection(Order<MongoDB>, "_id")
    - wrapper.addProjection(Order<MongoDB>, "customer_id")

db.order.aggregate( [ { $project : { "_id": 1, "customer_id": 1 } } ] )

queryPartB: {
    ?customer 2 ?customerName .
    ?customer 1 ?customerId .
}
    - wrapper.addProjection(Customer<PostgreSQL>, "name")
    - wrapper.addProjection(Customer<PostgreSQL>, "id")

```
SELECT id, name
FROM customer
```



## 5. Merging query parts

For each queryPart:
    results(queryPart) = execute(queryPart)

instanceCategory = {}
processedQueryParts = {}
For each joinPlan:
    If joinPlan.queryPartB not in processedQueryParts:
        instanceCategory.merge(joinPlan.queryPartB)
        processedQueryParts.add(joinPlan.queryPartB)
    If joinPlan.queryPartA not in processedQueryParts:
        instanceCategory.merge(joinPlan.queryPartA)
        processedQueryParts.add(joinPlan.queryPartA)

## 6. Execute delayed statements

For each delayedStatement:
    execute(delayedStatement)

## 7. Projection
