#!/usr/bin/python
# Filename: reference.py

print("Simple Assignment")
shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist is just another name pointing to the the same object
mylist = shoplist	

del shoplist[0]

print("shoplist is"), shoplist
print("mylist is"), mylist

print("shoplist is"), shoplist
print("mylist is"), mylist
# notice that shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print("Copy by making a full slice")
mylist = shoplist[:]	# make a copy by doing a full slice
del mylist[0]	# remove first item

print("shoplist is"), shoplist
print("mylist is"), mylist
# notice that now the twe lists are different
