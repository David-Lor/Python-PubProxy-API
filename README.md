# Python-PubProxy-API

A Python wrapper for the pubproxy.com public proxy API

## Limitations

When not using an API Key, pubproxy.com has a limit of 100 requests for hour. One execution of get_proxies is one request. Each request can return up to 20 proxies.

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
```
