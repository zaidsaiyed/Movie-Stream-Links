from justwatch import JustWatch
import json

country_name = 'CA'
just_watch = JustWatch(country=country_name)
user_input = input("Enter the movie name: ")

results = just_watch.search_for_item(query=user_input)
pro = just_watch.get_providers()

provider_dict = {}
for provider in pro:
    provider_dict[provider.get('id')] = provider.get('clear_name')

for i in results.get('items'):
    if i.get('offers') is None:
        continue
    print(f"{i.get('title')}:")
    
    for offer in i.get('offers'):
        provider_id = offer.get('provider_id')
        provider_name = provider_dict.get(provider_id, "Unknown Provider")
        monetization_type = offer.get('monetization_type')
        urls = offer.get('urls')
        
        if urls is None:
            continue
        for url_type, url in urls.items():
            print(f"{provider_name} - {monetization_type}: {url}")
    print("----" * 26)

with open('config.json', "w") as f:
    json.dump(results, f, indent=4)