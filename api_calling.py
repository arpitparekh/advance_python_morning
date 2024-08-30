# api
# to make a 2 way communication with server we need api

from requests import get

productList = []
randomUser = {}

url = "https://fakestoreapi.com/products"
url2 = "https://randomuser.me/api/"
response = get(url)
response2 = get(url2)

print(response.status_code)
productList = response.json()
randomUser = response2.json()
print(randomUser)

for i in productList:
  print('Title =',i["title"])
  print("Description = ,",i['description'])
  print("Price = ",i["price"])
  print("Image = ",i["image"])
  print()

for i in randomUser['results']:
  print(i['name']['first'],i['name']['last'])
  print(i['email'])
  print(i['gender'])
  print(i['location']['street']['number'],i['location']['street']['name'])
  print(i['location']['city'],i['location']['state'],i['location']['country'])
  print(i['location']['postcode'])
  print()

