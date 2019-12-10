# Monitoring

Keeping track of performance, health, and events of a service

KPIs - Key Performance Indicators

- Uptime - Is it up? Can people access the service? What is available?
- Resource utilisation (CPU, memory, network) - how taxing is running our app on the machine(s)?
- Throughput - how many requests are we serving per second? How much are we processing per second? This is the processing capacity.
- Errors - has something gone wrong? What has gone wrong?
- Business KPIs - not as tech driven; more to do with the problem domain, e.g. SkyBet: how many active users? To understand usage and how this relates to conversion to paid stuff.

```bash
$ uptime
13:44  up 26 days, 21:44, 4 users, load averages: 1.59 1.55 1.63
```

```bash
$ htop
```



Load average: a decimal number which tells you how busy your machine is

### Why?

- Take action before or at least as soon as things go wrong
- Understand actual application usage patterns (vs expected)
- Make more accurate business decisions
- Learn what normal (performance) looks like
- Assess the impact of our releases (like releasing a new feature): performance degradation, regressions, downtime...
- Identify areas in our architecture to improve (e.g. unsustainable performance, etc.)
- Make on-call work humnely possible

### What?

- Infrastructure - Is what is supporting your application ok?
- Applications - If your flask app is down, AWS will not tell you!
- Component interactions - what is talking to what? Are there any bottlenecks?

## Cloudwatch

AWS logs, monitoring and alerting managerd service. Offers:

- Log aggregation, retention and search
- Monitoring dashboards for AWS

### CloudWatch Metrics

a service which monitors and graphs the performance and health of your AWS infrastructure.

Most AWS manager services come with an assortment of predefined CloudWatch metrics.

You can create your own personalised monitoring dashboards and alerts.

### CloudWatch alarms

Send a notification when a performance/health threshold is exceeded.

Alarms notify you when things go wrong so that you can take corrective action as soon as possible.

Can be raised in a number of ways

CloudWatch Alarms can be raised in a number of ways:

- CloudWatch Alarms Dashboard
- Email (SNS - Simple Notification Service)
- Lambda

### SNS - Simple Notification Service

Fan out notoifications to different subscripbers via various channels, e.g. email, SMS, mobile push notification, Lambda.

Topic: notification category. You or an app can subscripte to it and get notified when a new event gets pushed to it. e.g. topic of 'object created in S3 bucket'

Subscription: sets the receiver of a notification and also dictates how they'll receive it.

## Logging

Added at key points at key areas of your codebase and can serve many different purposes. Events can be logged at different severity levels:

- Info: documenting the normal state changes in the app. Contains non-actionable information
- Warning: non-fatal errors, the kind of events you can leave until the next morning
- Errors: Fatal, kind of events you'd be woken up in the middle of the night to resolve. Means the application is unusable.

### When to use?

- Obtaining stack traces when or app crashes
- Tracing application flow
- Debugging our running application 
- App health monitoring
- Timing stuff precisely

### How to log?

Use a library. These remove much of the boilerplate and setup required to produce manageable logs.

We can tell a logger the type of error your would like to log (level), e.g. info, warning, error. We can also have different types of log levels written to different places, e.g. if you have a big error, you don't want to be looking at loads of info logs.

#### Python example

```python
import logging

logger = logging.getLogger(__name__)

try: 
  div = 1/0
except Exception as e:
  logger.exception(e)
```

#### Where do they go?

By default, the console/terminal output, so will therefore dissappear when the session is done.

To store our logs for future reference, we want to send them to a file.

```bash
$ python3 logger.py > app.log
```

Will make an empty app.log file! Need to use:

```bash
$ python3 logger.py &> app.log
```

Most applications have a default location where they store their log files.

Logs are usually stored in `/var/logs`

### Downsides

Log files will keep growing and growing so they'll require rotating (removing or archiving oldest logs).

Log files are only availbale in the server that produced them.

### Cloudwatch 

Can collate and store all of your logs for as long as you want so you don't have to worry about maintaining them.

Cloud watch > insights > your thing > logs

```sql
stats avg(timeMs)
  sort @timestamp desc
  filter ispresent(timeMs)
  limit 20
```

Query cloudwatch logs

```sql
fields event, level, message
	filter level = "info" and event = "app.init"
	sort @timestamp desc
```

CouldWatch Insights



Prometheus

Open source event monitoring and alerting tool used to collect custom metrics from apps.

Has a list of target HTTP endpoints

e.g. each of your applications prometheus is looking after will have some kind of metrics HTTP endpoint which prometheus will srcape on a regular basis (default 1 seconds). The results will be stored in a time-series database (local or remote) by Prometheus which can then be queried and potentially displayed usefully (e.g. by Grafana). 

```yaml
version:
services:
	prometheus:
	image: prom/pro
	prots:
		- "9090:9090"
	tty: true
	command: 
		- --config.file
		
	volumes:
		
```

Config file:

```yaml
global: 
	# Collect metrics
	
	
scrape_configs: 
# Prometheus can talk to itself to collect its own metrics
- job_name: "Prometheus"
```

### Grafana

Open source monitoring dashboard app w lots of features. 



Docker compose for grafana (appended to docker-compose for prometheus)

```yaml
[... prometheus docker-compose above ...]

grafana: 
	image: grafana:ver
	
```

Dockerfile to get this all good:

```dockerfile
ADD

EXPOSE
```

