num = int(input("Enter a number: "))

if num < -100:
    print("Negative large")

elif num < 0:
    print("Negative small")

elif num == 0:
    print("Zero")

elif num <= 100:
    print("Positive small")

else:
    print("Positive large")