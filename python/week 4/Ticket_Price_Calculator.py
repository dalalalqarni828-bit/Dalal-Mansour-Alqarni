age = int(input("Enter your age: "))
day = input("Enter the day: ")

if age < 12:
    price = 20

elif age < 18:
    price = 35

elif age < 60:
    price = 50

else:
    price = 25

if day == "Tuesday":

    price = price - 10

    if price < 10:
        price = 10

print("Final ticket price:", price, "SAR")