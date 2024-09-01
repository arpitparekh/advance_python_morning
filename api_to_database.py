# api integration
# application interface (web server)


# pip install requests

from requests import get
import mysql.connector


########################### database  ######################

db =  mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Walden0042$$",
  database = "python_morning_ronak"
)

cursor = db.cursor()

cursor.execute("create table if not exists product(name text, price varchar(255))")


###########################  api calling ###########################

url = "https://fakestoreapi.com/products"

productList = []

response = get(url)

print(response.status_code)

productList = response.json()   # convert jsoin to python list

for i in productList:
  name = i['title'].replace("'", "''")  # Escape single quotes
  price = i['price']
  cursor.execute(f"INSERT INTO product(name, price) VALUES ('{name}', '{price}')")

db.commit()
cursor.close()
db.close()
