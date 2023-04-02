from justwatch import JustWatch
import json

just_watch = JustWatch(country='CA')
user_input = input("Enter the movie name: ")

results = just_watch.search_for_item(query=user_input)
pro = just_watch.get_providers()

for i in results.get('items'):
    if i.get('offers') is None:
        continue
    print(i.get('title'))
    for offer in i.get('offers'):
        urls = offer.get('urls')
        if urls is None:
            continue
        for url_type, url in urls.items():
            print(f"{offer.get('provider_id')} - {offer.get('monetization_type')}: {url}")
    print("----" * 26)

with open('config.json', "w") as f:
    json.dump(results, f, indent=4)
