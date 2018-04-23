
import requests
import json

class Proxy(object):
    """A proxy object.
    Attributes:
        * ip - string
        * port - int
        * ip_port - string
        * country - string
        * last_check - string (date and time)
        * level - float
        * type - string (http, socks4, socks5)
        * speed - float
        Support tags:
        * https - bool
        * get - bool
        * post - bool
        * cookies - bool
        * referer - bool
        * user_agent - bool
        * google - bool (if can reach Google)
    """
    def __init__(self, js):
        """Proxy objects are initialized by the JSON get from pubproxy.com
        """
        self.ip = js["ip"]
        self.port = int(js["port"])
        self.ip_port = js["ipPort"]
        self.country = js["country"]
        self.last_check = js["last_checked"]
        self.level = js["proxy_level"]
        self.type = js["type"]
        self.speed = float(js["speed"])
        support = js["support"]
        self.https = bool(support["https"])
        self.get = bool(support["get"])
        self.post = bool(support["post"])
        self.cookies = bool(support["cookies"])
        self.referer = bool(support["referer"])
        self.user_agent = bool(support["user_agent"])
        self.google = bool(support["google"])

def get_proxies(api_key=None, level=None, protocol=None, last_check=None, limit=20, country=None, not_country=None, port=None, google=None, https=None, get=None, post=None, user_agent=None, cookies=None, referer=None):
    """Get a list of proxies from pubproxy.com. Return a list of Proxy objects.
    There's a limit of 100 requests per day without API key.
    :param api_key: optional API key for pubproxy.com
    :param level: anonymity level ('anonymous'/'elite')
    :param protocol: protocol/type of proxy ('http'/'socks4'/'socks5')
    :param last_check: get proxies verified not later than this time (minutes)
    :param limit: max. number of proxies to fetch (max. 20 without API Key)
    :param country: code or list of codes of countries to get proxies from
    :param not_country: code or list of codes of countries for NOT getting proxies from
    :param port: port of proxies
    :param google: get proxies that works on Google?
    :param https: get proxies that support HTTPS requests?
    :param get: get proxies that support GET requests?
    :param post: get proxies that support POST requests?
    :param user_agent: get proxies that support USER_AGENT requests?
    :param cookies: get proxies that support COOKIES requests?
    :param referer: get proxies that support REFERER requests?
    :return: list of Proxy objects
    """

    URL = "http://pubproxy.com/api/proxy?"
    loc = locals()
    
    #Append all attributes on API URL
    for key in tuple(v for v in loc if loc[v] is not None):
        if key in ("URL", "loc"):
            continue
        value = loc[key]
        
        if key in ("google", "https", "get", "post", "user_agent", "cookies", "referer"): #Bools must be converted to int
            value = int(value)
        
        elif key in ("country", "not_country"): #Convert countries lists to strings
            if type(value) is str:
                value = (value,)
            country_string = ""
            for c in value:
                country_string += "{},".format(c.upper())
            country_string = country_string[:-1] #Delete last ,
            value = country_string
        
        elif key == "protocol":
            key = "type"

        URL += "{}={}&".format(key, value) #Append key:value to URL
    
    URL = URL[:-1] #Delete last & from URL
    
    #Request to the API
    r = requests.get(URL).text

    #Extract data from the API, creating Proxy objects
    proxies = list()
    for j in json.loads(r)["data"]:
        proxies.append(Proxy(j))
    return proxies
