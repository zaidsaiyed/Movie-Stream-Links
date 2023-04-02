from justwatch import JustWatch
import json

    
just_watch = JustWatch(country='CA')
user_input = input("Enter the movie name: ")

results = just_watch.search_for_item(query = user_input)
pro = just_watch.get_providers()


for i in results.get('items'):
    if i.get('offers') is None:
        continue
    print(i.get('title'))
    off = (i.get('offers'))
    print(off[0].get('urls').get('standard_web'))
    print("----"*26)
with open('config.json', "w") as f:
    json.dump(results, f, indent=4)