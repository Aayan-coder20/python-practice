# print("--- Entrance Exam Students ---")
# print("List of Students:")

# cet = {"Alice", "Bob", "Charlie", "David"}
# jee = {"Eve", "Frank", "Grace", "Heidi"}
# neet =  {"Ivan", "Judy", "Karl", "Liam"}


# print("CET Students:", cet)
# print("JEE Students:", jee)
# print("NEET Students:", neet)

# all_students = cet.union(jee, neet)
# print("All Students:", all_students)

# all_exams = cet.intersection(jee, neet)
# print("All Exams:", all_exams)

# jee_not_neet = jee.difference(neet)
# print("JEE but not for NEET:", jee_not_neet)

# cet_neet_not_jee = cet.intersection(neet).difference(jee)
# print("CET and NEET but not for JEE:", cet_neet_not_jee)
# AIM: WAP to find students appearing for entrance exams

print("--- Entrance Exam Students ---")

cet_students = {"Bob", "Frank", "Charlie", "Alice"}
jee_students = {"Bob", "Heidi", "Frank", "Eve"}
neet_students = {"Bob", "Charlie", "Karl", "Liam"}

print("List of Students:")
print(f"CET Students: {cet_students}")
print(f"JEE Students: {jee_students}")
print(f"NEET Students: {neet_students}")

# All students appearing for any entrance exam
all_students = cet_students.union(jee_students, neet_students)
print(f"All Students: {all_students}")

# Students appearing for all entrance exams
all_exams = cet_students.intersection(jee_students, neet_students)
print(f"All Exams: {all_exams}")

# Students appearing for JEE but not for NEET
jee_not_neet = jee_students.difference(neet_students)
print(f"JEE but not for NEET: {jee_not_neet}")

# Students appearing for CET and NEET but not for JEE
cet_neet_not_jee = cet_students.intersection(neet_students).difference(jee_students)
print(f"CET and NEET but not for JEE: {cet_neet_not_jee}")

