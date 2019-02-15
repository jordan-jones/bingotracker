def input_checker():
    while True:
        input_coordinates = input('Enter value here: ')
        letter_coordinate = input_coordinates[0]
        number_coordinate = input_coordinates[1]
        is_valid = False

        if len(input_coordinates) != 2:
            print('{} is not a valid input, please try again.'.format(input_coordinates))
            continue
        elif not (letter_coordinate.isalpha() and number_coordinate.isdigit()):
            print('Oops, {} does not contain a letter and a number, please try again'.format(input_coordinates))
        else:
            print('{} is a correct format'.format(input_coordinates))
            is_valid = True
            break

input_checker()

