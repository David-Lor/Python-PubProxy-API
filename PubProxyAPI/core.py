
import requests
import json

class Proxy(object):
    """A proxy object
    """
    def __init__(self, js):
        """Proxy objects are initialized by the JSON get from pubproxy.com
        """
        self.ip = js["ip"]
        self.port = int(js["port"])
        self.ip_port = js["ipPort"]
        self.country = js["country"]
        self.last_checked = js["last_checked"]
        self.level = js["proxy_level"]
        self.type = js["type"]
        self.speed = int(js["speed"])
        support = js["support"]
        self.https = bool(support["https"])
        self.get = bool(support["get"])
        self.post = bool(support["post"])
        self.cookies = bool(support["cookies"])
        self.referer = bool(support["referer"])
        self.user_agent = bool(support["user_agent"])
        self.google = bool(support["google"])

def get_proxies(api_key=None, level=None, protocol=None, last_check=None, limit=20, country=None, not_country=None, port=None, google=None, https=None, get=None, post=None, user_agent=None, cookies=None, referer=None):
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
