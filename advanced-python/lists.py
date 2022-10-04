# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

#you can access an element by the index
item = mylist[1]
print(item)

# creates an empty list, later on you can append items
mylist2 = [5, True, "apple", "apple"]
print(mylist2)

#you can iterate through a list with a for in loop:
for i in mylist:
    print(i)

    if "banana" in mylist:
        print("yes")
    else:
        print("no")

print(len(mylist2))

mylist.append("lemon")
print(mylist)

mylist.insert(2, "blueberry")
print(mylist[3])

item = mylist.pop()
print("Popped item:", item)

print(mylist[::1])
print(mylist)