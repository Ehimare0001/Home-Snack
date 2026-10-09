import random
numbers = []

for i in range(10):
   
   numbers.append(random.randint(1, 50))
    
print("list:", numbers)

count = 0
for number in numbers:
    count = count + 1
    
print("length: ", count)


even_sum = 0
for i in range(0, count, 2):
    even_sum = even_sum + numbers[i]
print("Sum at even positions: ", even_sum)

odd_sum = 0
for i in range(1, count, 2):
    odd_sum = odd_sum + numbers[i]
print("Sum at odd positions: ", odd_sum)

product = 1
for i in range(2, count, 3):
    product = product * numbers[i]
print("Product at every third position: ", product)

average = 0
total = 0
for number in numbers:
    total = total + number
average = total/count
print("Average: ", average)

largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
return largest
print("Largest: ", largest)

smallest = numbers[0]
for number in numbers:
    if number < smallest:
print("Smallest: ", smallest)







