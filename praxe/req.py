import requests
from pprint import pprint
import json
from datetime import datetime

"""
r = requests.get("https://cat-fact.herokuapp.com/facts").json()

# pprint(r)

facts: dict[datetime, str] = {}
for fact in r:
    facts[datetime.strptime(fact["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")] = fact["text"]

# pprint(facts)

# get oldest fact
oldest_fact: str = facts[min(facts.keys())]

print(oldest_fact)

"""
r = requests.get("https://cat-fact.herokuapp.com/facts")

oldest_post = min(
    r.json(), key=lambda x: datetime.strptime(x["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
)

print(oldest_post["text"])
