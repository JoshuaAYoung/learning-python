show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    count = 0
    if which == "even":
        for num in numbers:
            if (num % 2 == 0):
                count = count + 1
    elif which == "odd":
        for num in numbers:
            if (num % 2 != 0):
                count = count + 1
    else:
        count = -1
    return count

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

count_numbers("even", numbers)
count_numbers("odd", numbers)
count_numbers("Blarg", numbers)