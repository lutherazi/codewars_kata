def iq_test(numbers):
    # It is necessary to separate the string using .split() 
    num = numbers.split()
    num_odd  = 0
    num_even = 0
    position = 0
    # It is necessary to create an even and odd number counter, to find out which one of the given numbers differs from the others
    for k, v in enumerate(num):
        if int(v) % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
    # Condition to know in which position the odd or even number is according to the counter
    if num_odd > num_even:
        for k, v in enumerate(num):
            if int(v) % 2 == 0:
                position = k + 1
    else:
        for k, v in enumerate(num):
            if int(v) % 2 != 0:
                position = k + 1
    print(position)


iq_test('2 4 7 8 10')
iq_test('1 2 2')