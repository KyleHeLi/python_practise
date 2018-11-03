import sys
import functions

print(sys.argv)

if "--help" in sys.argv:
    print("this is our super helpful help message")

if len(sys.argv[1:]) >= 2:
    print(functions.add_strings(sys.argv[1], sys.argv[2]))

print("a line")
print("next line")
print("another line")

functions.add_strings(sys.argv[1], sys.argv[2])

print("end of the program")
sys.exit()