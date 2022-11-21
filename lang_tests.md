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

