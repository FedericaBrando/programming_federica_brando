##################################################################
#               needleman and wunch algorithm                    #
#----------------------------------------------------------------#
#                          Pseudocode                            #
# 1_import dictionary                                            #
#   1.1_adding penalty                                           #
# 2_function for scorematrix:                                    #
#       - inizializzazione matrici vuote                         #
#       - indicizzazione matrice                                 #
#       - find the best score within last row and last column    #
#       - while cycle to iterate into the matrix (until row[i]=0 #
#         and col[i]=0                                           #
# 3_take input from user                                         #
# 4_recall functions                                             #
# 5_print in a readable way the output                           #
# (try to add ___main___)                                        #
##################################################################

from sys import argv
from input_data import * # seq1, seq2, BLOSUM52 are imported from input_data

def pen(D, penalty):
    """pen is a function that takes in input the dictionary and it add the given value for penalty"""
    aa = "ACDEFGHIKLMNPQRSTVWY"
    for am in aa:
        D[am + "-"] = int(penalty)
        D["-"+am] = int(penalty)

    return D

def n_w(Dic, seq1, seq2):
    col = len(seq1) + 1
    row = len(seq2) + 1
    F[[0] * col for x in range(row)]
    T[["0"] * col for x in range(row)]


