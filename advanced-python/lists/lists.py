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

#appends value at the end of
mylist.append("lemon")
print(mylist)

#inserts value at the 2 index
mylist.insert(2, "blueberry")
print(mylist[3])

#removes and returns last item of list
item = mylist.pop()
print("Popped item:", item)
print(mylist)

removed_item = mylist.remove("apple")
print(removed_item)

cleared_item = mylist2.clear()
print(cleared_item)

new_list = mylist + mylist2
print(new_list)