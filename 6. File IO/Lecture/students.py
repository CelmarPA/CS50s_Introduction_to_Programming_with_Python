import csv


# with open("students02.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")


# students = []
#
# with open("students02.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)


# students = []
#
# with open("students02.csv") as file:
#     for line in file:
#         name, home = line.rstrip().split(",")
#         student = {"name": name, "home": home}
#         students.append(student)


# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")


# def get_house(student):
#     return student["house"]
#
#
# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
#
#


# students = []
#
# with open("students02.csv") as file:
#     reader = csv.reader(file)
#
#     for name, home in reader:
#         students.append({"name": name, "home": home})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# students = []
#
# with open("students02.csv") as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")


# name = input("What's your name? ")
# home = input("Where's your home? ")
#
# with open("students.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])


name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

