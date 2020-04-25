import json

firstnames = []

with open("birthdays.json", "r") as f:
    info = json.load(f)

for x in info:
    firstnames.append(x)

print("\nWelcome to the birthday dictionary. We know the birthdays of:")
print(firstnames)

choice = input("\nDo you want to (add) to or (ask) for a birthday?: ")

if choice == "ask":
    ask = input("\nWhich birthday do you want to know?: ")
    if ask in info:
        print(f"The birthday is on the {info[ask]}")
        print("\n")
    else:
        print("\nThe birthday you ask for is not stored")

if choice == "add":
    name = input("\nWhose birthday do you want to add?: ")
    bday = input("\nWhats the persons birthday?: ")
    info[name] = bday
    print(info)
    with open("birthdays.json", "w") as f:
        json.dump(info, f)
