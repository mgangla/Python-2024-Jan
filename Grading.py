#python program that allows the user to enter the score of a student and assigns a grade from A to E

marks = float(input("Enter the student mark: "))

if marks > 80:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B")
elif marks >= 60 and marks < 70:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
else:
    print("Grade: E")