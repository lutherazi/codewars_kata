# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    phone_number = '('
    for k, v in enumerate(n):
        if k < 3:
            phone_number += str(v)
            if k == 2:
                phone_number += ') '
        elif k >= 3:
            phone_number += str(v)
            if k == 5:
                phone_number += '-'
    print(phone_number)


print('Phone Numbers:')
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111"
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890"
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000"
