#Q1
from typing import Dict

my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
print(my_dict.values())
print(my_dict.keys())
print(my_dict['name'])
my_dict['age']=32
print(f"the dictionary after modify age :",my_dict)
my_dict.update({ 'workplace':'GSG'})
print(f"the dictionary after adding new key and value :",my_dict)

#Q2
my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
new_dict=dict((x,y) for x,y in my_tuple)
print(f"Thr new dictionary is :",new_dict)

#Q3
dic1= {'name': 'Dema', 'age': 20}
dic2 = {'job': 'Engineer', 'ID': 456367}
dic3 = {'Year': 2003}
dictionary={}
dictionary.update(dic1)
dictionary.update(dic2)
dictionary.update(dic3)
print(dictionary)

#Q4
my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
max = -99
min= 99
for value in my_dict.values():
    if value > max:
        max=value
    if value < min:
        min=value

print(f"The maximum value is :",max)
print(f"The minimum value is:",min)

#Q5
my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
key_dict={'ID'}
print(key_dict.issubset(my_dict.keys()))

#Q6
Languages2023 = {
    'Programming Language': ['python', 'Java', 'JavaScript', 'C#'],
    'Market Share %': [27.99, 15.9, 9.36, 6.67]
}

keys = list(Languages2023.keys())
values = list(Languages2023.values())
list_dict= []

for x in range(len(values[0])):
    new_dict = {}
    for y in range(len(keys)):
        new_dict[keys[y]] = values[y][x]
    list_dict.append(new_dict)

print(list_dict)








