"""
Luke Mains
14.July.2018
TODO Fix memory usage stuff. Crashes your computer if it runs long enough
"""

# Functions


def list_factors(number):
    """
    Finds the
    :param number:
    :return:
    """
    factor_list = []

    for i in range(number):
        temp = float(number/(i+1))
        if temp.is_integer():
            factor_list.append(int(temp))

    return factor_list


def main():
    """
    The n'th triangle number is the sum of n natural numbers. This
    program calculates the factors of each triangle number and prints
    it if it has greater than 500 factors. Then it should stop but
    i'm not sure if it will.
    :return: None
    """

    number = 1

    for i in range(100000):
        number += i
        if len(list_factors(number)) > 500:
            print(number)
            break
    return


# ------------------------------------------- #


if __name__ == '__main__':
    main()
