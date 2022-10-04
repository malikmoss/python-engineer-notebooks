# Lists: ordered, mutable, allows duplicate elements
my_list = ["banana", "cherry", "apple"]
print(my_list)

#you can access an element by the index
item = my_list[1]
print(item)

# creates an empty list, later on you can append items
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

#you can iterate through a list with a for in loop:
for i in my_list:
    print(i)

    if "banana" in my_list:
        print("yes")
    else:
        print("no")

print(len(mylist2))