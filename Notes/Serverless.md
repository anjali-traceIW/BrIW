# Serverless

Abstraction of server provisioning servers. Paying for the convenience of being able to focus on 'the mission'. Is a service which we can think less about. Some cost benefits - when service not in use, don't have to pay. Abstraction of auto-scaling - don;t need to decide when autoscaling is necesary, amazon will do that for you.

Event-driven: need an event to trigger the exection of a lambda (a service) (?)F

Key components of serverless:

- Gateway (HTTP) - web-exposed entrypoints to an app
- Function - some logic executed (e.g. a lambda)
- Table - query-able data storage (e.g. RDS)
- Blob storage
- Queue - scheduling when to complete a job
- Stream - think reading a file stream in python. Start where you last stopped in the information.
- Workflow - describing the steps (e.g. these things) of what happens per process (think user stories). Step functions - use when your code is going to take arbitrarily long. 
- Lake (?)

So what is it? Service based, linear scaling, abstracted architecture.

Parallel execution of lambdas.

**Testing it?** Unit test it to death. Integration test are more difficult.

Amazon **SDK** - Software Development Kit

Other serverless technologies - Lambdas is most used one, but azure has (slightly different) things too.

protocol rest buffers

**Ideal usage** - cost can be a deciding factor, but is usually cheaper than alternatives,

Legacy technology can be less suitable - don't scale as well with greater load on serverless. Does require some initial architecture design overhead. Need to break something down into logical serverless components

Lambdas - the things holding the code and what will trigger it (e.g. a HTTP request).

Benefit - scales down to nothing. Not many things have zero cost when not in use. 

Not great for existing legacy code. Applications need to be built for serverless.

**Cons of serverless** - Running and testing locally is tricker.

- Limited (but growing) set of supporting languages
- Memory limit per lambda instance. If exceeeded, lambda is instantly and abruptly destroyed. This is due to the runtime manager allocating a hard limit per lambda to prevent your overflow affecting performance of running neighbours.

Multiple requests are handled by a docker instance of your lambda each (in parallel). Amazon's container manager will horizontally scale for you, starting up a new container per request (cold start). These containers can stick around for a while after completing (up to 4 hours for amazon), ready to receive another request (this is warming up your lambdas).

**Serverless with non-event-driven workloads**

What about workloads with strict, time-sensitive requirements which may have dramatic spikes in demand.

Extreme time-sensitive stuff is usually most reliably achieved by procuring your own hardware. More ideally, write in assembly to not rely upon programming language latency.

Can trigger a lambda with a load balancer.

