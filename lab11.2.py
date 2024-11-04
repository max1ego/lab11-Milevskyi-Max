import json

with open("phones.json", "r") as file:
    phones = json.load(file)

latest_year = max(phone["year"] for phone in phones)

latest_phones = [phone for phone in phones if phone["year"] == latest_year]

phones_sorted_by_price = sorted(phones, key=lambda x: x["price"])

cheapest_phones = phones_sorted_by_price[:3]

print("Найновіші телефони:")
print(json.dumps(latest_phones, indent=4, ensure_ascii=False))

print("\nНайдешевші моделі:")
print(json.dumps(cheapest_phones, indent=4, ensure_ascii=False))
