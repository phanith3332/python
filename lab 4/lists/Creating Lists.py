#list_1
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(len(list))

'''sample output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10 '''


#LIST_2
list=[12, 3.14, 'spring', True , ['example']]
for item in list:
    print("Value:", item, "Type:", type(item))

'''sample output:
Value: 12 Type: <class 'int'>
Value: 3.14 Type: <class 'float'>
Value: spring Type: <class 'str'>
Value: True Type: <class 'bool'>
Value: ['example'] Type: <class 'list'>
'''

#lists_3
list=[]
list.append(12)
list.append(23)
list.append(34)
list.append(45)
list.append(56)
print(list)

'''sample output:
[12, 23, 34, 45, 56]'''
