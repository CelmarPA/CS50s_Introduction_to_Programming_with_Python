students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# gryffindors = {student: "Gryffindor" for student in students}
#
# print(gryffindors)

for i, name in enumerate(students, start=1):
    print(i, name)
