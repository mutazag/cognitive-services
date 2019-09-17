# %%
import json
from pathlib import Path
import requests


#%%
secrets_file = Path("./bing-search/secrets.json")

if secrets_file.exists() is True:
    with open(secrets_file, "rt") as json_data: 
        secrets = json.load(json_data)

#%%
def getRequest(secrets, query): 
    request = f"{secrets['endpoint']}/search?q={query}&customconfig={secrets['config_id']}&count=50&mkt=en-US"
    print(request)
    header = {'Ocp-Apim-Subscription-Key':secrets['subscription_key1']}
    r = requests.get(request,headers=header)
    return r

#%%
r = getRequest(secrets,'training')
print(r.json)

#%%
resp = json.loads(r.text)
# print(json.dumps(resp, indent=2, sort_keys=True))

# %% 
webPages = resp['webPages']['value']
for w in webPages: 
    print(f"id: {'id' in w.keys()}, "
    f"searchTags :{'searchTags' in w.keys()}")
#%%
for w in webPages:
    print(f"url: {w['displayUrl']}")


#%%
