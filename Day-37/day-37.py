print("🌟Star Wars Name Generator🌟")
print("Easy version")
firstname = input("input your firstname?\n")
lastname = input("your lastname?\n")
mother = input("your mother's maiden name?\n")
city = input("and the city that you were born\n")
print(f"Your Star Wars name is {firstname[:4]}{lastname[:4]}{mother[:2]}{city[-3:]}")