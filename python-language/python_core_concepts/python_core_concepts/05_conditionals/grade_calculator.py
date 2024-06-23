# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

students_score : int = int(input("Enter Student Score"))

if students_score > 100:
    print("Enter Valid Input")
    exit()
else:
    if students_score > 89 and students_score <= 100:
        print("Grade : A")
    elif students_score > 79:
        print("Grade : B")
    elif students_score > 69:
        print("Grade : C")
    elif students_score > 59:
        print("Grade : D")
    else:
        print("Grade : F")