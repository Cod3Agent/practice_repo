    # This is a file to help me better myself on everything python related
    # To uncomment different lines, highlight them and use cmd + / on mac and ctrl + / on windows
# list1 = ["Dad", "Alex Hormozi", "Mark Zuckerberg"]

# print("I have found a bigger dinner table everyone!!")

# list1.insert(0, "Jimmy (Mr. Beast)")
# list1.insert(3, "Jensen (Nvidia CEO)")
# list1.append("Joe Bryant")

# print(f"Hello, {list1[0]}, you have been officially invited to my dinner party.")
# print(f"Hello, {list1[1]}, you have been officially invited to my dinner party.")
# print(f"Hello, {list1[2]}, you have been officially invited to my dinner party.")
# print(f"Hello, {list1[3]}, you have been officially invited to my dinner party.")
# print(f"Hello, {list1[4]}, you have been officially invited to my dinner party.")
# print(f"Hello, {list1[5]}, you have been officially invited to my dinner party.")

# print("Unfortunately I can now only invite two people to the event now.")

#l ist1.pop()
# list1.pop()
# list1.pop()
# list1.pop()

# print(f"Hello, {list1[0]}, you are still invited to my dinner.")

# print(f"Hello, {list1[1]}, you are still invited to my dinner")

# del list1[1]
# del list1[0]
# print(list1)

    # This is the second list, where I am learning how to sort.
# list2 = ['Ireland', 'Japan', 'Italy', 'Germany', 'Colorado']

# print(list2)

# list2.sort(reverse=True)
# print(list2)

    # Here I will use the first list.
# print(f"I am inviting {len(list1)} people to dinner.")





# get_list = ['Napkins','Apples','Oranges','Grapes','Peaches']
# length1 = len(get_list)
# print(f"Here is my get list {get_list}")
# \n creates a line break in python
# print(f"This is my list if I were to sort it: \n{sorted(get_list)}")
# print(f"this is it back to normal: \n{get_list}")
# get_list.sort()
# print(f"I like it better sorted: \n{get_list}")
# del get_list[0]
# print(f"I have gotten Apples. Here is the new list: {get_list}")
# get_list.remove("Napkins")
# print(f"I have also gotten napkins. Here is the updated list: {get_list}")
# popped_item = get_list.pop()
# print(f"I have gotten {popped_item}. Here is the new list: {get_list}")
# get_list.reverse()
# print(f"I have decided to get oranges first. Here is the new list: {get_list}")
# get_list.insert(0,"Balloons")
# print(f"I forgot that I need to get balloons. I will add it to my list as a top priority: \n{get_list}")
# get_list.append("Chocolate")
# print(f"I forgot that I also need to get chocolate. I'll add it to the top: \n{get_list}")
# length2 = len(get_list)
# print(f"The original length of my list was {length1} items long. Now it is {length2} items long.")


    # Working with loops

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# fav_pizzas = ['pepperoni', 'pepperoni and honey', 'meat lovers']

# for pizza in fav_pizzas:
#     print(f"I like {pizza} pizza.")
# print("Man I REALLY love pizza!")

# animals = ['sheep','goat', 'turkey']
# for animal in animals:
#     print(f"A {animal} is a good farm animal.")
# print(f"All of these animals are farm animals.ashdsjdj")


# sqaures = []
# for value in range(1,11):
#     sqaures.append(value**2)
# print(sqaures)

# # Learning list comprehension
# sqaures = [value**2 for value in range(1,11)]
# print(sqaures)

# print120 = [value for value in range(1,21,2)]
# print(min(print120))
# print(max(print120))
# print(print120)

# cubed =[value**3 for value in range(1,11)]
# print(cubed)

    # Working with slicing
# print(f"The first three items in this list are: \n")
# for num in cubed[:3]:
#     print(num)

# cubed =[value**3 for value in range(1,11)]
# print(cubed)

# print(f"The middle three items in this list are: \n")
# for num in cubed[3:7]:
#     print(num)

#     fav_pizzas = ['pepperoni', 'pepperoni and honey', 'meat lovers']

# for pizza in fav_pizzas:
#     print(f"I like {pizza} pizza.")
# print("Man I REALLY love pizza!")

# friend_pizza = fav_pizzas[:]
# fav_pizzas.append('turkey pizza')
# friend_pizza.append('goat pizza')

# print(fav_pizzas)
# print(friend_pizza)

# tuplefood = ('ham', 'mac', 'chicken', 'steak', 'rib')
# for food in tuplefood:
#     print(food)
    # example of what will throw an error for tuples
# tuplefood[0] = 'crab' will have a TypeError






# alien_color = 'green'

# if alien_color == 'green':
#     print('You just earned five points!')
# if alien_color != 'green':
#     print("Congratulations, you just earned 10 points!")

# alien_color = 'red'

# if alien_color == 'green':
#     print('You just earned five points!')
# elif alien_color == 'yellow':
#     print("Congratulations, you have just earned 10 points!")
# elif alien_color == 'red':
#     print("Congratulations, you have just earned 15 points!")

# age = 50

# if age < 2:
#     print("You are a baby!")
# elif 2 <= age <= 4:
#     print("You are a toddler!")
# elif 4 <= age <= 13:
#     print("You are a kid!")
# elif 13 <= age <= 20:
#     print("You are a teenager!")
# elif 20 <= age <= 65:
#     print("You are an adult!")
# else:
#     print("You are an elder!")





# fav_fruit = ['golden kiwi', 'watermelon', 'banana']

# if 'golden kiwi' in fav_fruit:
#     print("You really like golden kiwi's!")
# if 'pear' in fav_fruit:
#     print("You really like pears!")
# if 'watermelon' in fav_fruit:
#     print("You really like watermelons!")
# if 'Apple' in fav_fruit:
#     print("You really like apples!")
# if 'banana' in fav_fruit:
#     print("You really like bananas!")

# hello_admin = ['xmoore','smnoore','jbryant','wmoore','admin']
    # this will priint out the last else block | hello_admin = []
# if hello_admin:
#     for user in hello_admin:
#         if user == 'admin':
#             print('Hello admin, would you like to see a status report?')
#         else:
#             print(f'Hello {user}, thank you for logging in again.')
# else:
#     print('We need to find some users!')




# current_users = ['xmoore','smoore','jbryant','wmoore','admin']
# new_users = ['xavier','SMOORE','jbryant','wmoore','george']

# if new_users:
#     for new_user in new_users:
#         if new_user.lower() in current_users:
#             print('You will need to enter a new username. This one has already been used.')
#         else:
#             print("You have created your username.")
# else:
#     print('There are no new users.')




# num_list = [1,2,3,4,5,6,7,8,9]
# if num_list:
#     for num in num_list:
#         if num == 1:
#             print('1st')
#         elif num == 2:
#             print('2nd')
#         elif num == 3:
#             print('3rd')
#         elif num == 4:
#             print('4th')
#         elif num == 5:
#             print('5th')
#         elif num == 6:
#             print('6th')
#         elif num == 7:
#             print('7th')
#         elif num == 8:
#             print('8th')
#         elif num == 9:
#             print('9th')
# else:
#     print('This list is empty.')





# dict_person = {'first_name':'Skylar', 'last_name':'Moore', 'Age':'25', 'City':'Beattyville'}
# for key, value in dict_person.items():
#     print(key, value)

# three_river = {'nile':'egypt', 'red':'united states', 'mississippi':'united states'}
# for river, country in three_river.items():
#     print(f"The {river} river runs through the country {country}.")
# for river in three_river.keys():
#     print(river)
# for country in three_river.values():
#     print(country.title())

# favorite_languages = {
#     'skylar' : 'english',
#     'wendi' : 'spanish',
#     'jason' : 'french',
#     'xavier' : 'korean',
#     'joe' : 'mandarin',
# }

# should_take = ['skylar', 'wendi', 'fern', 'jim']
# for name in favorite_languages.keys():
#     if name in should_take:
#         print(f"Thank you {name} for taking the poll.")
#     else:
#         print(f"{name}, please take our poll!")
