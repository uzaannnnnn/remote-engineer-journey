def classification(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = classification(20)
print(result)

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

check = is_even(9)
print(check)

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "Minus"
    
grading = grade(80)
print(grading)