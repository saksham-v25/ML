#program to find maximum number from a list of number without using maximum funt and length functon


numbers=input("Enter the List of Numbers : ")
#33 34 44 54
numbers_list=numbers.split()
print(numbers_list)
count=0

for number in numbers_list :
    count=count+1

print(count)

for i in range(count):
    numbers_list[i] = int(numbers_list[i])

print(numbers_list)

maximum_number=numbers_list[0]
for number in numbers_list :
    if number > maximum_number :
        maximum_number = number


print(f"the maximum number is {maximum_number}")