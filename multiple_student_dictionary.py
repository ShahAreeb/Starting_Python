students = [
    {"Name": "Areeb", "Marks": 96},
    {"Name": "Rahul", "Marks": 72},
    {"Name": "Alex", "Marks": 81}
]

for student in students:
    print(student)

if students[0]["Marks"] > students[1]["Marks"] and students[0]["Marks"] > students[2]["Marks"]:

    print(f"The highest marks are obtained by {students[0]['Name']} with {students[0]['Marks']} Marks")

elif students[1]["Marks"] > students[0]["Marks"] and students[1]["Marks"] > students[2]["Marks"]:

    print(f"The highest marks are obtained by {students[1]['Name']} with {students[1]['Marks']} Marks")

else:

    print(f"The highest marks are obtained by {students[2]['Name']} with {students[2]['Marks']} Marks")