# Cross-Origin Resource Sharing and Same-Origin Policy cheat sheet 

## CORS and it's background

CORS is a sole browser concept to protect the user.  

CORS application means selective dogma violation.  

Dogma: "No other server will be inquired."  

CORS works via the backend http response headers warning the browser.  

CORS does not protect anything, it just warns the user's browser beforehand so the browser has the possibility to exercise a veto.  

## CORS implementation

```console
Access-Control-Allow-Origin
Indicates whether the response can be shared.

Access-Control-Allow-Credentials
Indicates whether the response to the request can be exposed when the credentials flag is true.

Access-Control-Allow-Headers
Used in response to a preflight request to indicate which HTTP headers can be used when making the actual request.

Access-Control-Allow-Methods
Specifies the methods allowed when accessing the resource in response to a preflight request.

Access-Control-Expose-Headers
Indicates which headers can be exposed as part of the response by listing their names.

Access-Control-Max-Age
Indicates how long the results of a preflight request can be cached.

Access-Control-Request-Headers
Used when issuing a preflight request to let the server know which HTTP headers will be used when the actual request is made.

Access-Control-Request-Method
Used when issuing a preflight request to let the server know which HTTP method will be used when the actual request is made.

Origin
Indicates where a fetch originates from.

Timing-Allow-Origin
Specifies origins that are allowed to see values of attributes retrieved via features of the Resource Timing API, which would otherwise be reported as zero due to cross-origin restrictions.
```
### 

The client can now exercise a veto and block according to it's wishes through it's forthcoming HTTP REQUESTS.
```console
GET
The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

HEAD
The HEAD method asks for a response identical to that of a GET request, but without the response body.

POST
The POST method is used to submit an entity to the specified resource, often causing a change in state or side effects on the server.

PUT
The PUT method replaces all current representations of the target resource with the request payload.

DELETE
The DELETE method deletes the specified resource.

CONNECT
The CONNECT method establishes a tunnel to the server identified by the target resource.

OPTIONS
The OPTIONS method is used to describe the communication options for the target resource.

TRACE
The TRACE method performs a message loop-back test along the path to the target resource.

PATCH
The PATCH method is used to apply partial modifications to a resource.


