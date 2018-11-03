# file = open("data/ioExample.fa", mode='r')
# for line in file:
#     print(line, end=" ")
#     # print(file.readline())
#
# file.close()

# initialize an empty list fro us to put data info
data = []

# get the data from the file
with open("data/ioExample.fa", mode = 'r') as file:
    for line in file:
        if line[0] == '>':
            line = line[1: -3]
            line = line.split(";")
            data.append(line)
            # print(line)#, end = " ")

replace_list = ['type=', 'loc=', 'ID=', 'name=', 'dbxref=', 'score=', 'score_text=', \
                'MD5=', 'length=', 'parent=', 'release=', 'species=']

with open("ioOut.tsv", mode = 'a') as output:
    for line in data:
        for field in line:

            # solution 1
            # for index in replace_list:
            #     if index in field:
            #         field = field.replace(index, ' ')

            # solution 2
            field = field.split("=")
            field = field[1]
            output.write(field + '\t')
        output.write('\n')

print("done!")
