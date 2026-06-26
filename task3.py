subjects = ["Python", "SQL", "Excel", "Tableau"]

print(subjects)

print(subjects[0])
print(subjects[-1])

subjects.insert(1, "Java")
print(subjects)

subjects.remove("Excel")
print(subjects)

new_list = subjects.copy()
print(new_list)

new_list.sort()
print(new_list)

if "Excel" in new_list:
    print("Excel is present in the list.")
else:
    print("Excel is not present in the list.")