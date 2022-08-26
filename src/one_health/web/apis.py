import requests
import json

URLS = "https://newsapi.org/v2/everything?q=medical&from=2022-07-26&sortBy=publishedAt&apiKey=bd48bd00db6d4feab29c5a6aa5582cd0"



resul = requests.get(URLS)
data = json.loads(resul.text)


totalResult = data['totalResults']
articles= data['articles']
source= data['articles'][2]
print(f"la source: ", source)
for art in articles:
    list_result = (
        f"l\'autheur est: {art['author']}",
        f"le titre: {art['title']}", 
        f"la description: {art['description']}"
    )
    print( list_result)



