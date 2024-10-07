"""Practice making for...in...loops!"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for animal in pets:
    # "animal" is the "elem" - can name it anything!
    print(f"Good boy, {animal}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    # print each index: name
    print(f"{idx}: {names[idx]}")
