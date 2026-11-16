# This is a file to help me better myself on lists
list1 = ["Dad", "Alex Hormozi", "Mark Zuckerberg"]

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
