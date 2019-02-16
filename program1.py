import re
entries = list('')
menu_selection = ''
allowed_chars = set('BINGO')
maximum_number = 75
pattern = "^[bingoBINGO]\d{2}$"

def input_checker(): # Check for a valid entry
    while True:
        input_coordinates = input('Enter value here (type "qq" to quit): ')
        letter_coordinate = input_coordinates[0]
        number_coordinate = input_coordinates[1]
        is_valid = False

        if input_coordinates == 'qq':
            print('qq entered. Quitting application...')
            break
        elif not re.search("[a-zA-Z](\d{2})",input_coordinates):
            print('Failed on REGEX validation')
        elif not set(letter_coordinate.upper()).issubset(allowed_chars):
            print('{} does not contain the correct letters, please try again'.format(letter_coordinate))
        elif len(input_coordinates) != 2: # checks that it is two characters long
            print('{} is not a valid input, please try again.'.format(input_coordinates))
            continue
        elif not (letter_coordinate.isalpha() and number_coordinate.isdigit()): # check that the first character is a letter and the second character is a number
            print('Oops, {} does not contain a letter and a number, please try again'.format(input_coordinates))
        else:
            print('{} is a correct format'.format(input_coordinates))
            entries.append(input_coordinates.upper())
            print(entries)

input_checker()
