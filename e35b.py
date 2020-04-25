import json
from collections import Counter

january = 0

with open("birthdays.json", "r") as f: # Är detta "as file"?
    info = json.load(f)

sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]

mackor = {"Daniel": "februari", "Andre": "juli", "Bengt": "oktober", "Berra": "mars",
"Kenta": "september","Bosse": "februari", "Klas": "augusti", "V6": "juli", "Kossan mu":
"december", "Johan": "juli"}

if "februari" in mackor:
        print("Yes")
