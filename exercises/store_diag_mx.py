####################################################################################################
# 4) Write a script that stores into a Python dictionary a substitution matrix in diagonal format. #
####################################################################################################
#                                  one rule game: DO NOT USE LISTS.                                #
####################################################################################################

def get_nth_key(dictionary, n):  # indicizza il dizionario n è un intero
    if n < 0:
        newn = input('n must be grater than 0, please insert a new number: ')
        return get_nth_key(dictionary, int(newn))
    elif n > len(dictionary):
        print("Index out of range! n must be between 0 and", len(dictionary))
        newn = input('insert new n : ')
        return get_nth_key(dictionary, int(newn))
    else:
        for i, key in enumerate(dictionary):
            if i == n:
                return key


def scoring_dic():
    #filepath = input('insert the path file for the scoring matrix: ')
    filepath = '../data/PAM250.txt'
    sc_mx_file = open(filepath, 'r')
    aa = sc_mx_file.readline()
    aa = aa.split()

    sc_dict = {}
    for aa1 in aa:
        for aa2 in aa:
            print(aa1,aa2)
            if sc_dict[aa2+aa1] not in sc_dict:
                sc_dict[aa1+aa2] = 0
            print(aa1+aa2)

    print(sc_dict)

    # i = 0
    # while i < len(sc_dict):  # fin tanto che i è minore di len(sc_dict) in questo caos 400
    #     line = sc_mx_file.readline()
    #     line = line.split()
    #     line = line[1:]
    #     for val in line:
    #         sc_dict[get_nth_key(sc_dict, i)] = float(val)
    #         i += 1
    return sc_dict


print(scoring_dic())