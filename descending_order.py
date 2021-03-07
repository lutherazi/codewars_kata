# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
# Essentially, rearrange the digits to create the highest possible number.
def descending_order(num):
    order = int(''.join(map(str, sorted([i for i in str(num)], reverse=True))))
    print(order)


print('Testing...')
descending_order(0)
descending_order(51)
descending_order(123456789)
