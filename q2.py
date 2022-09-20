##########################
#                        #
# IS111 Quiz #2  Q2      #
#                        #
##########################
#
# Name: Lucerne Loke
# Email ID: lucerne.loke.2022
#

def change_case_n_timesx(text, n):
    # Replace the code below with your implmentations.
    if n == 0:
        return text

    str_list = list(text)
    for i in range(len(str_list)):
        if n == 0:
            break
    
        if str_list[i].isalpha():
            str_list[i] = str_list[i].lower()
            n -= 1
    
    return ''.join(str_list)

def change_case_n_times(text, n):
    return ''.join([((list(text)[i].lower()) if list(text)[i].isalpha() and n > 0 else list(text)[i]) for i in range(len(list(text)))])
    # cannot n -= 1