# Microservices

> Wednesday 2nd October 2019 (Week 5)

A monolith: a complex, tightly coupled, heavily self-reliant code base. Pitfalls:

- End up with areas of work overlapping, means plenty of conflicts and unforseen regressions in unrelated places.
- More difficult to understand.
- Lots of coordination to release a new version. Can be risky if a well-used and depended upon application.
- Unable to optimise or scale effectively.

## Microservices

A single-purpose appplcation with a bounded context.

<u>Not</u> a distributed monolith.

### Microservice Architecture

- Single-purpose
- RESTful APIs
- Small
- Networked

#### Boudaries

Having a bounded context means the microservice is standalone and doesn't need any knowledge of other microservices to do its job. As a rule of thumb: if microservices have to be deployed all at once, they're not loosely coupled.

#### Advantages

- Each squad owns their own microservice end-to-end
- Can evolve quickly
- Independent release schedules
- Can use different programming languages and frameworks
- Can run on optimum hardware per service
- Can scale efficiently
- Less likely to break unrelated things
- Enforces clear data exchange interfaces.
- Simpler and easier to understand hte unit

Strangle-hold pattern to refactor a monolith into microservices.

#### Disadvantages

- Language barriers: when microservices are written in diffferent languages, may be parts of the team who don't know the language, so cannot as easily maintain/access it.
- Data flow not obvious: in a monolith data integrity is somewhat assured and well known.
- Initial design and operational overhead.
- More intercommunication.
- Harder to design.
- Network latency.
- Conway's Law - organisational structure will reflect the services you maintain.
- Security

Rules of distributed computing: 

1. Distribute as little as possible
2. 

