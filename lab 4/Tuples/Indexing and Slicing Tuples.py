#tuple_4
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple[0])
print(tuple[5])
print(tuple[-1])

'''sample output:
1
6
10 '''

#tuple_5
numbers=(1,21,31,41,51,61,7,17,27,37,47,57)
print('first half:',numbers[:6])
print('secoend half:',numbers[6:])

'''sample output:
first half: (1, 21, 31, 41, 51, 61)
secoend half: (7, 17, 27, 37, 47, 57) '''

#tuple_6
colors=('green','orange','pink','red','white','yellow')
if 'green' in colors:
    print('this color exists in the given tuple')
else:
    print('this color is not exists in the given tuple')
    
'''sample output:
this color exists in the given tuple  '''

#tuple_7
numbers=(45,67,25,87,9,9,90,60,34,78,9)
print('minimum:',  min(numbers))
print('maximum:',max(numbers))
print('count of 9:',numbers.count(9))

'''sample output:
minimum: 9
maximum: 90
count of 9: 3  '''
