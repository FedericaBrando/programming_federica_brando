#!~/anaconda3/envs/PB/bin/python
# FINAL EXAM SCRIPT - FEDERICA BRANDO
# To build the Score and trace matrices, following Smith and Waterman algorithm:
# F(row,col), P(col, row)  = max{[F(row-1, col-1) + dict_score, "diag"]
#                               [F(row-1, col) + gap_penalty, "up"]
#                               [F(row, col-1) + gap_penalty, "left"]
#                               [0, "Z"]}
#pseudocode:
# sw_matrix(sequence1, sequence2, dictionary, gap_score):
#      - initialize Score and Traceback mx filled w/ 0
#      - initialize Traceback mx first column and first row w/ respectively 'up' and 'left'
#      - double for loop for SW algorithm
#      - return score and traceback matrices
# max_index(Score) and thresh_index functions(Score, threshold_value):
#      - for loop through the whole Score matrix to find best local ali in the first case
#        or local ali above threshold, in the second case
# sw_ali(score, traceback, sequence1, sequence2, threshold value):
#      - check threshold value: if 0 then max_index is performed, otherwise thresh_index is performed
#      - for loop that iterates the list of indexes found in the previous step
#      - while loop, until score_value == 0, checks traceback matrix value
#      - for each for loop appends to list_align, the tuple [string_template, string_intra, string_target, int_score]
#      - it returns list_align

from input import blosum50
import sys


def sw_matrix(seq1, seq2, dic, gap):
    """a) Function that takes in input the two sequences (seq1,seq2), the scoring dictionary and the gap value, it
    computes the scoring matrices F and the traceback matrix P and returns them in output"""
    C = len(s1) + 1  # col
    R = len(s2) + 1  # row
    F = [[0] * C for x in range(R)]  # list comprehension makes a list of lists filled with 0s CxR
    P = [['0'] * C for x in range(R)]  # makes another list of lists filled with '0'

    # init first row
    for righe in range(R):
        P[righe][0] = 'u'

    # init first col
    for colonne in range(C):
        P[0][colonne] = 'l'

    for row in range(1, R):
        for col in range(1, C):
            sR = F[row - 1][col] + int(gap)                                 # Smith and Waterman algo,
            sD = F[row - 1][col - 1] + dic[seq1[col - 1] + seq2[row - 1]]   # for each i,j pos in each matrix, a list of tuple coupled w/
            sC = F[row][col - 1] + int(gap)                                 # the corresponding letter is created and compared
            sG = 0                                                          # with itself to find the maximum
            zippa = list(zip((sC, sR, sD, sG), ("l", "u", "d", "Z")))
            final = max(zippa)                                              # result is assigned to final
            F[row][col], P[row][col] = final                                # final[score, letter] is added to the matrices
    return F, P


def max_index(F):
    """Function that takes in input the score matrix, finds the highest scores throughout the whole matrix and
    stores into a list of tuples the indexes of the scores"""
    c = len(F[0])                               # n° of columns
    r = len(F)                                  # n° of rows
    max_score = F[0][0]                         # init max_score
    max_out = []
    for col in range(1, c):
        for row in range(1, r):
            temp_score = F[row][col]            # temporary score assigned to temp_score
            if temp_score > max_score:          # if temp_score is greater than max_score, max_score is reassigned
                max_score = temp_score
                max_out = [[row, col]]          # max_out has its indexes
            elif temp_score == max_score:
                temp_coord = [row, col]
                max_out.append(temp_coord)      #if there is more than one value w/ the same score, indexes are added
    return max_out

def thresh_index(F, th):
    """Function that takes in input the score matrix and the threshold, finds the scores above the threshold and
    stores into a list of tuples the indexes of the scores"""
    c = len(F[0])                            # n° of columns
    r = len(F)                               # n° of rows
    max_out = []
    for col in range(1, c):
        for row in range(1, r):
            temp_score = F[row][col]         # temporary score assigned to temp_score
            if temp_score >= th:             # if temp_score is greater or equal to the threshold then
                temp_coord = [row, col]      # its indexes are stored in temp_coord (type: tuple) and then
                max_out.append(temp_coord)   # appended to a list of tuple
    if max_out == [] :
        return print("\nthreshold value is too high")  # if threshold is too high, function tells it to the user

    return max_out


def sw_align(F, P, seq1, seq2, th_value = 0):
    """ b) Function that takes F, P, seq1 and seq2 as input and returns a list of tuples of the best local alignment(s)
    between seq1 and seq2 and the corresponding score(s). If threshold is present, it returns all the local alignment(s)
    above that threshold"""
    if th_value <= 0 :                          # If threshold value is 0 or negative, then the function will
        mx_index = max_index(F)                 # compute the BEST local alignment(s)
    else:
        mx_index = thresh_index(F, th_value)    # if threshold value is greater than 0, the function will retrieve
                                                # all those local alignments with score above the threshold
    align = []
    for i in range(len(mx_index)):
        row, col = mx_index[i]
        score = F[row][col]
        template = ''                           # Initialization of empty strings that will store
        target = ''                             # template, target and symbols in between template and target seq
        intra = ''
        while F[row][col] != 0:                 # until the value of F(i,j) is NOT 0 do it enters the while loop
            if P[row][col] == 'd':              # takes into account the traceback matrix (P), if the letter is 'd'
                template += seq1[col - 1]       # it goes back in diagonal way, row and column change
                target += seq2[row - 1]
                intra += '|'
                row -= 1
                col -= 1
            elif P[row][col] == 'l':            # if the values is 'l' it goes back on the left (column changes
                template += seq1[col - 1]       # row does not change)
                target += '-'
                intra += ' '
                col -= 1
            elif P[row][col] == 'u':            # if the values is 'u', it goes back in the up direction (row
                template += '-'                 # changes, column does not change)
                target += seq2[row - 1]
                intra += ' '
                row -= 1
        align += [[template[::-1], intra[::-1], target[::-1], score]]  # string are all reversed because it was going back

    return align

def print_ali(final_ali):
    '''Function that takes in input the alignment(s) and prints them accordingly'''
    for i in range(len(final_ali)):
        print(final_ali[i][0], final_ali[i][1], final_ali[i][2],  sep='\n')
        print('Alignment score:', final_ali[i][3], '\n')


if __name__ == "__main__":
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    gap = sys.argv[3]
    th = sys.argv[4]

    score, trace = sw_matrix(s1, s2, blosum50, gap)

# print matrices
#     for l in score:
#         print(l)
#     for col in trace:
#         print(col)

    final_align = sw_align(score, trace, s1, s2, int(th))
    print_ali(final_align)