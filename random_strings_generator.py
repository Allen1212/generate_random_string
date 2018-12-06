import random
import string


def random_strings_type(type_index, randomlength):
    if type_index == 0:
        str_list = [random.choice(string.digits) for i in range(randomlength)]
    elif type_index == 1:
        str_list = [random.choice(string.ascii_letters) for i in range(randomlength)]
    elif type_index == 2:
        str_list = [random.choice(string.ascii_lowercase) for i in range(randomlength)]
    elif type_index == 3:
        str_list = [random.choice(string.ascii_uppercase) for i in range(randomlength)]
    elif type_index == 4:
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    elif type_index == 5:
        str_list = [random.choice(string.digits + string.ascii_lowercase) for i in range(randomlength)]
    elif type_index == 6:
        str_list = [random.choice(string.digits + string.ascii_uppercase) for i in range(randomlength)]
    return str_list


def random_strings_generator(type_n, randomlength, numbers):
    strings = []
    if randomlength == 0:
        for index in range(numbers):
            randomlength = random.randint(1, 60)
            # print(randomlength)
            random_str = ''.join(random_strings_type(type_n, randomlength))
            if not random_str in strings:
                strings.append(random_str)
                # print(strings)
    else:
        for index in range(numbers):
            random_str = ''.join(random_strings_type(type_n, randomlength))
            if not random_str in strings:
                strings.append(random_str)
                # print(strings)

    with open("random_strings_file_%s.txt" % numbers, "w") as f:
        for item in strings:
            f.write('%s\n' % item)
        f.close()


type_index = int(input('Please choose the type of the string:\n' 
                '(0) digits\n' 
                '(1) letters\n' 
                '(2) lowercase\n' 
                '(3) uppercase\n' 
                '(4) digits + letters\n' 
                '(5) digits + lowercase\n'
                '(6) digits + uppercase\n'))


randomlength = int(input('Please input the length of random string(0 means random size of string from 1 to 20):\n'))
numbers = int(input('Please input the number of random string:\n'))
random_strings_generator(type_index, randomlength, numbers)

# randomlength = 0
# number = [50, 500, 5000, 50000]
# for numbers in number:
#     random_strings_generator(type_index, randomlength, numbers)



