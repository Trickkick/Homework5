import json
import csv

users_headers = ["name", "gender", "address", "age"]
data = []
some_user = []
books = []
user_counter = 0
result_data = []

with open("files/books.csv", newline='') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        books.append(row)

with open("files/users.json", "r") as json_file:
    str1 = json_file.read()
    users = json.loads(str1)

for user in users:
    for header in users_headers:
        some_user.append(user[header])
    some_user.append([])
    data.append(some_user)
    some_user = []

for book in books:
    data[user_counter][4].append(book)
    user_counter += 1
    if user_counter == len(data):
        user_counter = 0

users_headers.append("books")

for user in data:
    result_data.append(dict(zip(users_headers, user)))

print(result_data)

with open("files/result.json", "w") as f:
    json.dump(result_data, f, indent=4)
