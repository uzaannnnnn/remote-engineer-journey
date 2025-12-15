scores = [10, 70, 80, 90, 30]
passed = 0

for score in scores:
    if score >= 60:
        passed += 1
    
print("Passed Students: ",passed)

def count_even(numbers):
    count = 0
    for number in numbers:
        if number %2 == 0:
            count += 1
    
    return f"The Number of Even Numbers is {count}"

value = [1,2,3,4,5,6,7,8,9,10]
check = count_even(value)
print(check)