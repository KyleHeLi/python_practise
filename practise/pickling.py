#!/usr/bin/env python
# Filename: pickling.py

import cPickle as p
# import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist1 = ['apple', 'mango', 'carrot']
shoplist2 = ['Coke', 'Sprite', 'Ice Tea']

# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist1, f)	# dump the object to a file
p.dump(shoplist2, f)
f.close()

del shoplist1 	# remove the shoplist
del shoplist2

# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
storedlist += p.load(f)
print storedlist