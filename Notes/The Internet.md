## The Internet

(!!!)

### Network Protocols

A **protocol** is a standardised set of rules for two parties to follow in order to engage in a communicative activity.

A **network** protocol is a <u>standardised</u> way on which two computers exchange information.

The two key parties in web communication are the client and the serve.

#### Server

- Stored resorces and serves them requested
- "Publicly" available - e.g. this could be restricted to a network
- On 24/7

#### Client

- Request resources (websites, documents, pictures, etc.)
- Can be other servers (e.g. front end to an API) or an end user's device
- May connect t servers unpredictabilly

#### How do Network Protocols work?

Like matryoshka dolls - packages in packages. Each layer has a task/purpose.

The OSI model/network stack - 7 layers of abstraction.

We are interested in the Network (3), Transport (4), and Application layers (7)

##### Network (Internet Protocol IP)

Willl locate computers in a network and will try to deliver packets to them, but makes no promises. Private and public IPs.

Traceroute 

IP is just best effort, so how do we reach somewhere like google.com every time? How do we ensure our requests reach the right place every time?

#### Transport

TCP Transfer Control Protocol

Makes sure all data reaches its destination in an orderly fashion (not necessarily timely). IP is about as reliable as carrier pigeons. Volume for assurance. TCP regulates the pigeon-full sky.

#### HTTP 7

HyperText Transfer Protocol

Identifies a resource and what the client wants to do with it. i.e. which HTTP verb? (GET, POST, etc.)

DNS (Layer 7)

Domain Name Service

Creates a mapping (translates) human-friendly names (infinityworks.com) to IP addresses (54.192.33.91)

```bash
# Gives IP address of a given human-readable address
nslookup infinityworks.com
# Will also gives the DNS server holding that mapping
```

**infinityworks**.<u>com</u> 

**second-level somain**.<u>top-level domain</u>

### HTTP Messsages

#### Structure

HTTP messages have two parts:

##### Headers

Message metadata, e.g. type of content, length of content, source and destination hosts, cookie.

##### Payload

Message contents: JSON, etc.

#### Response codes:

- 1xx: info
- 2xx: success
- 3xx: redirect
- 4xx: Client errors
- 5xx: Server errors

#### HTTPS

All information exchanged between the client and the server in HTTP will be transmitted as plaintext, which is a big security problem.

#### TLS

Transport Layer Security

Formerly, mistakenly, known as SSL, used to secure the information exchange between two computers over a network. Is confidential. The illustrated guide to TLS.

Server must provide a HTTPS certificate to prove they are legit. Cost money except from lets encrypt (?)

### Web Servers

servers which understand TCP and HTTP protocols (and others)

Constantly listening for new requests so they can hand out information (pages, files, etc) to clients on request.

Nginx, Apache, IIS

Apache - does a lot, each slowly

Nginx - Does less but much faster. Lightwight, efficient reverse proxy used to serve web content

IIS - don't

##### Set up

brew install nginx