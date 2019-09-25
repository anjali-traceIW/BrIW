# APIs

> Tuesday 24th September 2019 (Week 4)

Application Programming Interface

JSON JavaScript Object Notation

REST REpresentational State Transfer

6 constraints must be satisfied to be considered RESTful:

- Client-server separation
- Stateless
- Cacheable resources
- Uniform Interface
- Layered system
- (Optional) code on demand

## A REST request

- Endpoint - made up of root, path, parameters (and port sometimes) `https://root/path?params`

- Method - GET, POST (make new), PUT (update or create if doesn't exit), PATCH (changing a little bit of a thing), DELETE

- Header - metadata about the request e.g. 

- ```json
  {
    "content-type : application/json"
    "user : test1"
  }
  ```

- Body: the content. The information you want to send to a server

## Curl

```bash
curl -X <request type> -H <header values> -d <"{json string}" or content file address>

curl -X POST localhost:8080 -H "Content-Type:application/json" -d "{"First_name": "Bob", "Last_name":"The Builder"}" 
```

