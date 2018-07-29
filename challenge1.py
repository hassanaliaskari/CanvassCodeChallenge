import math


# Checks if digits in a number are even
# Returns boolean of the check and returns smallest place-value of the odd digit
def are_digits_even(num):
    factor = 1
    while num >= 1:
        digit = num%10
        if digit%2 == 1:
            return (False, factor)
        num = math.floor(num/10)
        factor *= 10

    return (True, -1)


# Returns a list of numbers between 'start' and 'end' (inclusive) whose digits are all even
def get_even_digit_numbers(start, end):
    numbers = []
    number = start
    while number <= end:
        is_valid_number, factor = are_digits_even(number)
        if is_valid_number == True:
            numbers.append(number)
            number += 2
        else:
            number += factor

    return numbers


numbers = get_even_digit_numbers(1000, 3000)
print(*numbers, sep=",")

