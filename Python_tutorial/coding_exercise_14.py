#program to calculate average height from a list of height (dont use sum and length function ,use for loop to replicate functionalities)#

heights = input("enter all height separated by a space :")
#151 153 140 160  167

height_lists = heights.split()
count = 0
for height in height_lists :
     count = count + 1
print(count)

for i in range (0,count) :
    height_lists[i]=int(height_lists[i])
total = 0
for person in height_lists :
    total = total + person
avg = total/count
print("average heights is:",round(avg))