def sum_even_numbers(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total