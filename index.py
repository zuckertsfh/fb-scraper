import json
import csv, datetime
from facebook_scraper import get_profile, get_posts

jsonData = []

for post in get_posts('nintendo', pages=1):
    jsonData.append(post)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

jsonString = json.dumps(jsonData, default=myconverter)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()