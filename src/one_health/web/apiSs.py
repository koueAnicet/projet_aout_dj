from datetime import date
import requests
import json
import random

URLS = "https://newsapi.org/v2/everything?q=medical&from=2022-09-01&sortBy=publishedAt&apiKey=bd48bd00db6d4feab29c5a6aa5582cd0"
API_KEY="apiKey=bd48bd00db6d4feab29c5a6aa5582cd0"
URL1_SPECIALITY="https://newsapi.org/v2/everything?q="
URL2_DATA_PUBLISHING="https://newsapi.org/v2/everything?q=medical&from="

resul = requests.get(URLS)
data = json.loads(resul.text)


#totalResult = data['totalResults']
articles= data['articles']
print(articles)
source= data['articles'][1]

print( date.today())

v =  random.choices(articles, k=4)
print("@@@@@@@-------@@@@@\n")
print(v)

# for art in articles:
#     list_result = (
#         f"la source est: {art['source']['name']}\n",
#         f"l\'autheur est: {art['author']}\n",
#         # f"le titre: {art['title']}\n", 
#         # f"la description: {art['description']}\n"
#         # f"l\'url: {art['url']}\n"
#         # f"l\'urlToImage: {art['urlToImage']}\n"
#         # f"la date publication: {art['publishedAt'].isoformat()}\n"
#         # f"le contenu: {art['content']}\n"
#     )
#     print( list_result)
