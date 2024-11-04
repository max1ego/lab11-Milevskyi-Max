import csv

num_authors = 15  

authors = []
for _ in range(num_authors):
    name = input("Введіть прізвище автора: ")
    birth_year = int(input("Введіть рік народження автора: "))
    authors.append((name, birth_year))

authors.sort(key=lambda x: x[1])

with open("authors.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    for author in authors:
        writer.writerow(author)

