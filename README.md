# Python-PubProxy-API

A Python wrapper for the pubproxy.com public proxy API

## Limitations

When not using an API Key, pubproxy.com has a limit of 100 requests per day. Each execution of get_proxies is one request. Each request can return up to 20 proxies.

## Examples

```python
    from PubProxyAPI import get_proxies

    #Get all proxies
    proxies = get_proxies()

    #Get proxies from Spain and France
    proxies = get_proxies(country=["ES","FR"])

    #Get proxies from everywhere EXCEPT United States
    proxies = get_proxies(no_country="US")

    #Get up to 5 Socks5 proxies from US, on port 80
    proxies = get_proxies(country="US", port=80, protocol="socks5", limit=5)

    #Get proxies that were last checked less than 5 minutes ago, that support GET and POST requests
    proxies = get_proxies(last_check=5, get=True, post=True)

    #Get up to 10 anonymous proxies from everywhere except France and Spain, that support GET, POST and Cookies, that work on Google
    proxies = get_proxies(limit=10, no_country=("FR","ES"), get=1, post=1, cookies=1, google=1)
```
