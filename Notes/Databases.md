# Databases

A collection of structured infrormation of data accessible for convenient use.

## Utilisation

(R)DBMS **R**elational **D**ata**b**ase **M**anagement **S**ervices

SQL **S**trutured **Q**uery **L**anguage

THE language for querying relation databases

Declarative, not imperative

```sql
--SELECT records from a table
SELECT <*/column_names> FROM <table_name> WHERE <condition> ORDER BY <columns_name>

--INSERT a new record into a table
INSERT INTO <table_name> (<column_names>) VALUES (<corresponding_values>)

--UPDATE a field for some records
UPDATE <table_name> SET <column> = <value> WHERE <other_column> = <other_value>

--DELETE records in a table
DELETE FROM <table_name> WHERE <column> = <value>
```

## DML vs DDL

**D**ata **M**anipulation **L**anguage

What we've ben looking at so far.

**D**ata **D**efinition **L**anguage

How we create, alter, and drop tables.

```sql
--CREATE a new table
CREATE TABLE <table_name> (
		<column name> <type> (AUTO_INCREMENT) (PRIMARY KEY),
  	<column2 name> <type>,
  	...
);

--ALTER a table
ALTER TABLE <table_name> ADD <column_name> <type>;

--DROP a table
DROP TABLE <table_name>;
```

To set a connection for our My SQL cli: 

```bash
$ mysql -h < host_name> -u < user_name > -p
```

### JOIN

**INNER JOIN** returns rows matching the condition of the join

**LEFT/RIGHT OUTER JOIN** returns the matching data of A and B as well as everything from (LEFT: A/ RIGHT: B)

**FULL OUTER JOIN** returns everything from both tables, regardless of if they match.

## NoSQL

Non-relational databases. Still actually ise SQL.

- ColumnarDBs
- Key-Value DBs
- GraphDBs

We like them because:

- Dynamic schema - no set structure
- Auto-sharding - distribution of data across servers
- Auto replication - allows for high availablility (master/slave?)
- The move to distributed sercives makes a monolith DB overkill
- Easily scalable - more servers means more replication and load balancing (adding nodes vs expanding underlying architecture)

Good at things like user sessions, games, caches - things with single modular information. Doesn't work well handling relations, asking for joined data is quite difficult.

CosmoDB is a hybrid?

Some examples

- MogoDB
- HBase
- DynamoDB
- Cassandra

## Object Relational Mapper (ORM)

An abstraction layer for the database interaction. You interact directly with objects (like the rest of your code) and behind the scenes it will generate the SQL. Get to reference things by object refs.

Can be super powerful, but often heavy weight. Often overused and abused.

Lack of exact control over details of execution.