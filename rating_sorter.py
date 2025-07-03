import csv
from pprint import pprint

with open("students.csv", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    students = list(dict_reader)

students.sort(key=lambda x: int(x["score"]), reverse=True)

pprint(students)

with open("rating.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["rank", "name", "score"])

    for i, student in enumerate(students, start=1):
        writer.writerow([i, student["name"], student["score"]])
