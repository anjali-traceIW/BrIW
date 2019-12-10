# More AWS Services

## Relational database service (RDS)



## Identity and Access Management (IAM)

- Manage users and thier access 
- Manage roles permissions for the roles
- Manage authentication for users accessing aws
- Free to use - can create as many roles as you wish.

### Concepts

- Principle of least privilege
- Manage groups - a user can belong to a group
- Manage users - e.g. a person
- Manage roles - a user can assume or be assigned a role

#### Users

For a given user, can manage:

- the accounts that habe access
- security credentials e.g. MFA. Manage the permissions of what the user can perform.

#### Roles

- Can be assumed by users or other AWS services
- Specific permissions on AWS sercies and resources
- Policies are attached to roles to grant hthem access/privilege

#### Best practices

- users - create indiv users
- groups - Manage permissions with groups
- permissions - grant least privilege
- auditing - can be achieved aws cloud trail

## CLI

How we interact with AWS services through the CLI. Ease over use over logging into the console. If you can do it on the console, you can do it in the CLI (YAY!). Simple use cases: seacrching logs, quick s3 upload/download

## DynamoDB

The true webscale data store

How do we scale out a data store? How do we design a database to be optimised for read vs write?

DynamoDB is a NoSQL document/key-value data store with an emphasis on resilience. Mongo-DB uses a JSON-like document to store data. 

- Global and (virtually) unlimited storage - available everywhere and replicated across the globe.
- Highly available - data is durable: specifically optimised to retain data during outages etc.
- Highly scalable and elastic - can accommodate dramatic changes in demand/load/user traffic and scale accordingly.
- Simple API interface
- Fast
- Not necessarily consistent

Recall CAP thm

**ACID** - Atomic Consistent Isolated, and Durable - set of properties that guarentee that database transactions are processed reliably. 'ACID transactions'

### DynamoDB Table Structures

Table - not what you think of in the RDS sense

Items "Rows"

Attributes - "Fields" or "Columns"

But you could have item1 with attributes {name, age, job} and item2 with attributes {name, happy?, birthday}. Is schema less. Does still have a unique identifier ("a primary key") e.g. name from above.

DynamoDB is a lot faster than MySQL because it's webscale(??)

#### Accessing data

Items are stored and accessible by their primary key = {partition key: how items are grouped together, sort key: introduces a sorting dimension and enriches queries}

#### Usage

You do not 'log in' to Dynamo. Talk to it via dynamo api or sdks or manually vs aws console

- `GetItem` fetch item by prim key
- `PutItems` upsert an item into the teable
- `Query` fetch subset of a table
- `Scan` return entire contents of a table 

#### Limitations

Low latency, but only if the data structures and queries have been carefully optimised for it. Not too flexible. You will need to know your data access patterns (what it looks like and how you will want to retrieve it) in advance of setup. No such thing as joins or relationships in DynamoDB, so cannot easily retrospectively retrieve relational data stored in two different tables. 

Only simple queries. 

Inflexible schema.

#### Use Cases

Well-suited for repeatable, consistent, **non-relational** data workloads with very high throughput demands.

- IoT - lots of identical devices with unique information which is unlikely to be needed in relation to one another
- Gaming: leaderboards/player session info - quick retrieval/updating times for live calculations.
- Mobile: user profiles, personalisation settings
- Web: customer preferences, session info, shopping basket contents (?). 

Amazon's Well-Architected Framework

More? Get certified!

AWS Cloud Practitioner - entry level, academy-level knowledge?

AWS Solutions Architect - Assoc.