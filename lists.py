import pprint

# LISTS

# arr = [1, 2, 3]
# arr = arr * 3
# print(arr)
# cat = 'cat'
# cat = list(cat)
# print(cat)

supplies = ['pens', 'dogs', 'lion', 'pencils']

# works no matter what length of list is
for i in range (len(supplies)):
    print('Index ' + str(i) + ' supply is: ' + supplies[i])


utensil, pet, animal, supply = supplies
print(animal)

supplies.insert(1, 'bat')
supplies.append('el chico')
print(supplies)

numbers = [1,6,9,7]
numbers.sort(reverse=True)
print(numbers)

# DICTIONARIES

myCat = {
    'size': 'fat',
    'pets': 2,
    'house': False
}

print(myCat)
print(myCat.keys())

for k in myCat.keys():
    print(k)
for v in myCat.values():
    print(v)
for i in myCat.items():
    print(i)

print(myCat.get('dogs', 'none'))

myCat.setdefault('color', 'red')
print(myCat)
 
message = 'It was a hobbit hole, bilbo baggins'
count = {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char] + 1

pprint.pprint(count)
