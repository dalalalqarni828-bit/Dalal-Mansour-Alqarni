student = {"name": "Ali", "age": 17, "grade": "11"}

print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])

print("_" * 30 + "\n" )

prices = {"apple": 3, "banana": 2}

prices["mango"] = 5
prices["apple"] = 4

print(prices)

print("_" * 30 + "\n" )

user = {
    "name": "Sara",
    "email": "sara@example.com",
    "city": "Jeddah"
}

print("Keys:", list(user.keys()))
print("'name' in dict:", "name" in user)
print("'phone' in dict:", "phone" in user)