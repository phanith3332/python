#tuple_1
countries=('India', 'Russia','France', 'Germany', 'Japan')
print('countries:', countries)
print('type:',type(countries))
print('lenghth:', len(countries))

'''sample output:
countries: ('India', 'Russia', 'France', 'Germany', 'Japan')
type: <class 'tuple'>
lenghth: 5  '''

#tuple_2
element=('single',)
print('tuple:',element)
print('type:',type(element))

'''sample output:
tuple: ('single',)
type: <class 'tuple'>  '''

#tuple_3
numbers=[12,13,14,15,16]
tuple=tuple(numbers)
print('list: ',numbers)
print('tuple: ',tuple)
new_list=list(tuple)
print('converted list: ',new_list)

'''sample output:
list:  [12, 13, 14, 15, 16]
tuple:  (12, 13, 14, 15, 16)
converted list:  [12, 13, 14, 15, 16]  '''
