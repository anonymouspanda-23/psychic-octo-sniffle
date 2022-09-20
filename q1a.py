##########################
#                        #
# IS111 Quiz #2  Q1a     #
#                        #
##########################
#
# Name: Lucerne Loke
# Email ID: lucerne.loke.2022
#

def check_ascending_number(number):
    # Replace the code below with your implmentations.
    numbers_list = list(str(number))
    numbers_list = [int(num) for num in numbers_list]
    num_numbers = len(numbers_list)

    for i in range(num_numbers - 1):
        number1 = numbers_list[i]
        number2 = numbers_list[i + 1]
        if number1 >= number2:
            return False
    
    return True
