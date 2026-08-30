#tuple_8
integers=(90,80,70,60,50,40)
veg=('tamoto','cucumber','brinjal','drumstick','bitter guard')
add=integers+veg
repeat=integers*3
print('concatinating two tuples:',add)
print('repeating tuple 3 times:', repeat)

'''sample output:
concatinating two tuples: (90, 80, 70, 60, 50, 40, 'tamoto', 'cucumber', 'brinjal', 'drumstick', 'bitter guard')
repeating tuple 3 times: (90, 80, 70, 60, 50, 40, 90, 80, 70, 60, 50, 40, 90, 80, 70, 60, 50, 40)  '''

#tuple_9
marks=(91,94,96,92,97)
m1,m2,m3,m4,m5=marks
average=(m1+m2+m3+m4+m5)/5
print('marks:', m1,m2,m3,m4,m5)
print('average:',average)

'''sample output:
marks: 91 94 96 92 97
average: 94.0  '''

#tuple_10
numbers=(11,22,33)
try:
    numbers[0]=77
except TypeError as error:
    print('error:',error)

'''saple error:
error: 'tuple' object does not support item assignment  '''

#tuple_11
#tuples containg list
data=(10,20,[30,40],50,60)
#modify the nested list
data[2].append(70)
#the tuple is immutable,but the list inside it is mutable
print('updated tuple:', data)

'''sample output:
updated tuple: (10, 20, [30, 40, 70], 50, 60) '''

#tuple_12
numbers=(28,89,24,82,79)
sorted_numbers=sorted(numbers)
print('atcual tuple:', numbers)
print('sorted tuple:', sorted_numbers)

'''sample output:
atcual tuple: (28, 89, 24, 82, 79)
sorted tuple: [24, 28, 79, 82, 89]  '''



