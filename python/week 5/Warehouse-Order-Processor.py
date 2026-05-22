inventory = {
    "laptop": 5,
    "mouse": 10,
    "keyboard": 0
}

orders = [
    ("laptop", 2),
    ("mouse", 15),
    ("keyboard", 1),
    ("monitor", 3),
]

for product, qty in orders:

    match (product, qty):

        case (product, qty) if product not in inventory:
            print(f"{product}: not in inventory")

        case (product, qty) if inventory[product] >= qty:
            inventory[product] -= qty

            print(
                f"{product}: shipped {qty}, "
                f"{inventory[product]} left"
            )

        case (product, qty):
            print(
                f"{product}: only {inventory[product]} "
                f"in stock, cannot ship {qty}"
            )
