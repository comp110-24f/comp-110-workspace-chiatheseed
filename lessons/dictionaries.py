"""Practice w dictionaries!"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates # of key-value entries
print(len(ice_cream))

# add key-value entries using subsctiption notation
ice_cream["mint"] = 10

# access values by their key using subscription notation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# reassign values by their key using assignment operators
ice_cream["mint"] += 1

# remove items by key using pop method
ice_cream.pop("strawberry")

# test if key is in the dict;
print("vanilla" in ice_cream)
# returns True!
print("strawberry" in ice_cream)
# returns False!

# loop thru items using in loops
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")
