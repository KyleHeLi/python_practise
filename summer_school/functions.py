def adder(x, y = 10):
    '''
    Add a couple of numbers together

    :param x: this is a numer
    :param y: this is another number
    :return: result
    '''
    return x + y

def add_strings(str1, str2):
    '''
    Add the strings as if they were a number

    :param str1: string 1
    :param str2: another string
    :return: prtin the string
    '''
    return float(str1) + float(str2)

print(adder(4, 5))

print(adder(5))
