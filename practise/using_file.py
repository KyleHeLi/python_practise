#!/usr/bin/env python
# Filename: using_file.py

# poem = '''
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
# 	use Python!
# '''

# f = file('poem.txt', 'w')	# open for 'w'riting
# f.write(poem)	# write text to file
# f.close()	# close the file

# f = file('poem.txt')
# # if no mode is sepcified, 'r'ead mode is assumed by default
# while True:
# 	line = f.readline()
# 	if len(line) == 0:	# Zero length indicates EOF
# 		break
# 	print line,
# 	# Notice comma to avoid automatic newline added by Python
# f.close()	# close the file

file = open("testfile.txt", "a")

file.write("Hello World\n")
file.write("This is our new text file\n")
file.write("and this is another line.\n")
file.write("Why? Because we can.\n")

file.close()

with open("testfile.txt", mode="w") as file:
    lines_of_text = ["One line of text here", "and another line here",
                     "and yet another here", "and so on and so forth"]
    lines_of_text = [x + "\n" for x in lines_of_text]
    file.writelines(lines_of_text)

with open("testfile.txt", mode="r") as file:
    for line in file:
        # print("%s" % line.split())
        print("%s" % line.strip())

with open("testfile.txt", mode="w") as file:
    lines_of_text = ["One line of text here", "and another line here",
                     "and yet another here", "and so on and so forth"]
    file.writelines(lines_of_text)
