import mysql.connector

# pip install mysql-connector-python

db =  mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Walden0042$$",
  database = "python_morning_ronak"
)

if db.is_connected():
    print("Connected")
else:
    print("Not connected")


cursor = db.cursor()

# create table
cursor.execute("create table if not exists student(id int, name varchar(255))")

# insert data
# id = input("Enter id : ")
# name = input("Enter name : ")
# cursor.execute(f"insert into student(id,name) values ({id},'{name}')")

# print("Data Inserted Successfully in Database")

# data fetch
cursor.execute("select * from student")
data = cursor.fetchall()

for i in data:
    print(i)

db.commit()
cursor.close()
db.close()
