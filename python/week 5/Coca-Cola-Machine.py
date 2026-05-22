price = 50
amount_due = price

while amount_due > 0:

    coin = input("Insert Coin: ")

    if not coin.isdigit():
        print("Please insert a valid integer coin")
        continue

    coin = int(coin)

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        print(f"Amount Due: {amount_due}")
        continue

    amount_due -= coin

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

change = abs(amount_due)
print(f"Change Owed: {change}")