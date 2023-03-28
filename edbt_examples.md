# Query 1

```
SELECT {
    ?order itemId ?itemId ;
        status ?status ;
        customerName ?name ;
        city ?city .
}
WHERE {
    ?order 10 ?id ;
        11 ?status ;
        12/14 ?itemId ;
        9 ?customer .

    ?customer 2 ?name ;
        4/7 ?city .

    FILTER(?name = "Alice")
    VALUES ?status {"completed" "shipped"}
}
```

- Query spans multiple DBs
- Includes DB-level and cross-DB joins
- Has FILTER and VALUES
- Compound morphisms

# Query 2

```
SELECT {
    ?customer name ?name ;
        surname ?surname .
}
WHERE {
    ?customer 1 ?id ;
        2 ?name ;
        3 ?surname .
}
```

- Look at both single-DB query plans
- Data redundancy

# Query 3

```
SELECT {
    ?customer name ?name ;
        surname ?surname ;
        street ?street ;
        city ?city ;
        zipCode ?zipCode .
}
WHERE {
    ?customer 1 ?customerId ;
        2 ?name ;
        3 ?surname ;
        4 ?address .

    ?address 5 ?addressId ;
        6 ?street ;
        7 ?city ;
        8 ?zipCode .
}
```

- Single-DB join
- Multiple query plans (single-DB and multi-DB)
- Default plan and _6 plan

# Query 4

```
SELECT {
    ?address street ?street ;
        surname ?surname .
}
WHERE {
    ?address 5 ?id ;
        6 ?street ;
        -4/3 ?surname .
}
```

- Reverse morphism traversal + compound morphism
