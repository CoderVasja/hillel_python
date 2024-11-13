count = 0
while count == 0:
    string = input("Enter string with h or H: ")
    if 'h' in string:
        count = 1
        print('Fine we found "h"')
    elif 'H' in string:
        count = 1
        print('Fine we found "H"')
    else:
        print('h or H not found try again')