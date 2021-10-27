#https://datatracker.ietf.org/doc/html/rfc1945
#URI = scheme:[//authority]path[?query][#fragment]

# browser connects via string input dns->(dns resolve via ips cache or root server->tld server->authoritative name server)ip to server with tcp/ip (and ssl/tls for https to sign client and server)
# browser sends http request over tls/tcp to server ip (request line(verb, path, version\r\n)headers(name(user-agent, host, accept, X-...): value)\r\n)
# server sends back https response to browser over tls/tcp (version, 200 OK\r\n, headers (Content-Type, Set-Cookie,)\r\n,!DOCTYPE html>)

### IMPORT LIBRARIES ###

import requests

### GET request

x = requests.get("https://youtube.com/")

print(x.text)

### POST requests

# x = requests.post("https://google.com/", data=dict(
#    email="me@domain.com",
#    password="secret_value"
#))

### URL parameters

#r = requests.get("http://example.com/page", params=dict(
#    query="web scraping",
#    page=2
#))
