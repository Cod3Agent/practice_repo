# This is a file to help me better myself on lists
"""list1 = ["Dad", "Alex Hormozi", "Mark Zuckerberg"]

print("I have found a bigger dinner table everyone!!")

list1.insert(0, "Jimmy (Mr. Beast)")
list1.insert(3, "Jensen (Nvidia CEO)")
list1.append("Joe Bryant")

print(f"Hello, {list1[0]}, you have been officially invited to my dinner party.")
print(f"Hello, {list1[1]}, you have been officially invited to my dinner party.")
print(f"Hello, {list1[2]}, you have been officially invited to my dinner party.")
print(f"Hello, {list1[3]}, you have been officially invited to my dinner party.")
print(f"Hello, {list1[4]}, you have been officially invited to my dinner party.")
print(f"Hello, {list1[5]}, you have been officially invited to my dinner party.")

print("Unfortunately I can now only invite two people to the event now.")

list1.pop()
list1.pop()
list1.pop()
list1.pop()

print(f"Hello, {list1[0]}, you are still invited to my dinner.")

print(f"Hello, {list1[1]}, you are still invited to my dinner")

del list1[1]
del list1[0]
print(list1)

# This is the second list, where I am learning how to sort.
list2 = ['Ireland', 'Japan', 'Italy', 'Germany', 'Colorado']

print(list2)

list2.sort(reverse=True)
print(list2)

# Here I will use the first list.
print(f"I am inviting {len(list1)} people to dinner.")





get_list = ['Napkins','Apples','Oranges','Grapes','Peaches']
length1 = len(get_list)
print(f"Here is my get list {get_list}")
print(f"This is my list if I were to sort it: \n{sorted(get_list)}")
print(f"this is it back to normal: \n{get_list}")
get_list.sort()
print(f"I like it better sorted: \n{get_list}")
del get_list[0]
print(f"I have gotten Apples. Here is the new list: {get_list}")
get_list.remove("Napkins")
print(f"I have also gotten napkins. Here is the updated list: {get_list}")
popped_item = get_list.pop()
print(f"I have gotten {popped_item}. Here is the new list: {get_list}")
get_list.reverse()
print(f"I have decided to get oranges first. Here is the new list: {get_list}")
get_list.insert(0,"Balloons")
print(f"I forgot that I need to get balloons. I will add it to my list as a top priority: \n{get_list}")
get_list.append("Chocolate")
print(f"I forgot that I also need to get chocolate. I'll add it to the top: \n{get_list}")
length2 = len(get_list)
print(f"The original length of my list was {length1} items long. Now it is {length2} items long.")
"""

# Working with loops
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

fav_pizzas = ['pepperoni', 'pepperoni and honey', 'meat lovers']

for pizza in fav_pizzas:
    print(f"I like {pizza} pizza.")
print("Man I REALLY love pizza!")

animals = ['sheep','goat', 'turkey']
for animal in animals:
    print(f"A {animal} is a good farm animal.")
print(f"All of these animals are farm animals.ashdsjdj")


sqaures = []
for value in range(1,11):
    sqaures.append(value**2)
print(sqaures)

# Learning list comprehension
sqaures = [value**2 for value in range(1,11)]
print(sqaures)

print120 = [value for value in range(1,21,2)]
print(min(print120))
print(max(print120))
print(print120)
"""

"""
cubed =[value**3 for value in range(1,11)]
print(cubed)

# Working with slicing
print(f"The first three items in this list are: \n")
for num in cubed[:3]:
    print(num)

cubed =[value**3 for value in range(1,11)]
print(cubed)

print(f"The middle three items in this list are: \n")
for num in cubed[3:7]:
    print(num)

    fav_pizzas = ['pepperoni', 'pepperoni and honey', 'meat lovers']

for pizza in fav_pizzas:
    print(f"I like {pizza} pizza.")
print("Man I REALLY love pizza!")

friend_pizza = fav_pizzas[:]
fav_pizzas.append('turkey pizza')
friend_pizza.append('goat pizza')

print(fav_pizzas)
print(friend_pizza)

tuplefood = ('ham', 'mac', 'chicken', 'steak', 'rib')
for food in tuplefood:
    print(food)
# example of what will throw an error for tuples
# tuplefood[0] = 'crab' will have a TypeError






alien_color = 'green'

if alien_color == 'green':
    print('You just earned five points!')
if alien_color != 'green':
    print("Congratulations, you just earned 10 points!")

alien_color = 'red'

if alien_color == 'green':
    print('You just earned five points!')
elif alien_color == 'yellow':
    print("Congratulations, you have just earned 10 points!")
elif alien_color == 'red':
    print("Congratulations, you have just earned 15 points!")
"""

age = 50

if age < 2:
    print("You are a baby!")
elif 2 <= age <= 4:
    print("You are a toddler!")
elif 4 <= age <= 13:
    print("You are a kid!")
elif 13 <= age <= 20:
    print("You are a teenager!")
elif 20 <= age <= 65:
    print("You are an adult!")
else:
    print("You are an elder!")





fav_fruit = ['golden kiwi', 'watermelon', 'banana']

if 'golden kiwi' in fav_fruit:
    print("You really like golden kiwi's!")
if 'pear' in fav_fruit:
    print("You really like pears!")
if 'watermelon' in fav_fruit:
    print("You really like watermelons!")
if 'Apple' in fav_fruit:
    print("You really like apples!")
if 'banana' in fav_fruit:
    print("You really like bananas!")
