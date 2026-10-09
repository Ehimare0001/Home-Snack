numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def add_third(numbers):
    total = 0
    
for count in range(2, len(numbers), 3):
    total = total + numbers[count]
return total

print(add_third(numbers))

