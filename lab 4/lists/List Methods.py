 #list_11
 num=[11,22,33,44,55,66,77]
num.append(99)
print(num)
num.insert(3,88)
print('after inserting:', num)
num.extend([12,23])
print('after extend:', num)
num.remove(22)
print('after removing 22:', num)
num.pop()
print('after pop:', num)
num.sort()
print('sorting order:', num)
num.reverse()
print('reverse order:', num)
print('count of 55 is',num.count(55))
print('index of 33:', num.index(33))

'''sample output:
[11, 22, 33, 44, 55, 66, 77, 99]
after inserting: [11, 22, 33, 88, 44, 55, 66, 77, 99]
after extend: [11, 22, 33, 88, 44, 55, 66, 77, 99, 12, 23]
after removing 22: [11, 33, 88, 44, 55, 66, 77, 99, 12, 23]
after pop: [11, 33, 88, 44, 55, 66, 77, 99, 12]
sorting order: [11, 12, 33, 44, 55, 66, 77, 88, 99]
reverse order: [99, 88, 77, 66, 55, 44, 33, 12, 11]
count of 55 is 1
index of 33: 6  '''

#lists_12
numbers=[67,57,34,57,67,77]
result=[]
for num in numbers:
    if num not in result:
        result.append(num)
print(result)

'''sample output:
[67, 57, 34, 77] '''

#lists_13
numbers=[22,53,71,92,19,45]
maximum=numbers[0]
minimum=numbers[0]
total=0
for num in numbers:
    if num>maximum:
        maximum
    if num<minimum:
        minimum=num
    total+=num
print("maximum=", maximum)
print("minimum=", minimum)
print("sum=", total)

'''sample output:
maximum= 92
minimum= 19
sum= 302  '''

#lists_14
list1=[25,26,27,28]
list2=[39,40,41,42]
merged=list1 + list2
merged.sort(reverse=True)
print("merged sort:", merged)

'''sample output:

erged sort: [42, 41, 40, 39, 28, 27, 26, 25]  '''
