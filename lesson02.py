import math

# import test_lib
# from test_lib import *


def my_first_function(text):
    print('My first function get: ', text)
    return text


def summ(list_):
    summ_of_list = 0
    for n in list_:
        summ_of_list+=n
    return  summ_of_list


def mean(list_):
    return summ(list_) / len(list_)


def polyndrome(n):
    n_ = n
    n_copy = 0
    while n > 0:
        n_temp = n % 10
        n_copy = n_copy*10+n_temp
        n = int(n/10)
    if n_ == n_copy:
        return True
    else:
        return False


def polyndrome_2(n):
    # str(n)
    # n[::-1]

    return n == int(str(n)[::-1])


if __name__ == '__main__':
    # a = int(input())
    # string = my_first_function(math.sqrt(a))
    # print(string)

    # a = list()
    # a.append(int(input()))
    # i = 0
    # while True:
    #     a.append((int(input())))
    #     if a[-1] == 0:
    #         break
    #     # i+=1
    # print(summ(a))
    # print(mean(a))

    print('Yes') if polyndrome_2(1234321) else print('No')
