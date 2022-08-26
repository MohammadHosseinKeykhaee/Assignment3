#add to another list
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers2 = []
for n in numbers:
    numbers2.append(n**2)

print('Original list:', numbers)
print('power ^2 list:', numbers2)