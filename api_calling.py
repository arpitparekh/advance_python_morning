# api
# to make a 2 way communication with server we need api

from requests import get

productList = []

url = "https://fakestoreapi.com/products"
response = get(url)

print(response.status_code)
productList = response.json()

for i in productList:
  print('Title =',i["title"])
  print("Description = ,",i['description'])
  print("Price = ",i["price"])
  print("Image = ",i["image"])
  print()


