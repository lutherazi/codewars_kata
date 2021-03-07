# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = reversed(s)
    s = ''.join(s)
    print(int(s))


print('Testing...')
descending_order(0)
descending_order(51)
descending_order(123456789)
