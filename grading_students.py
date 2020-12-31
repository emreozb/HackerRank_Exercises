import math

grades = [84, 29, 57, 38]

round_grades = []
for grade in grades:
    if grade < 38:
        round_grades.append(grade)
    elif grade >= 38:
        if ((5*math.ceil(grade/5)) - grade) < 3:
            round_grades.append((5*round(grade/5)))
        else:
            round_grades.append(grade)
print(round_grades)




