###################################################################################
# pseudo code
# given two sequences of lenght m and n
# 1) build a matrix filled with zero with (mxn)
# 2) init 1st row and 1st col f(i,0) and f(0,i)
# iteration f(0,0) = 0
# f(i,j) = max
# return f
##################################################################################


def matrix_dict(matrix_file):
    l = []
    for line in matrix_file:
        line = line.rstrip()
        row = line.split()
        l.append(row)
    d = {}
    for i in range(1, len(l)):
        for j in range(0, len(l[0])):
            d[l[i][0] + l[0][j]] = int(l[i][j + 1])
    return d


def score_trace(s1, s2, mx_sc, pen):
    C = len(s1) + 1  # row
    R = len(s2) + 1  # col
    F = [[0] * C for x in range(R)]  # list comprehension makes a list of list filled with 0s MxN
    P = [['0'] * C for x in range(R)]  # makes another list filled with '0'

    # init first row
    for righe in range(R):
        P[righe][0] = 'u'

    # init first col
    for colonne in range(C):
        P[0][colonne] = 'l'

    P[0][0] = '0'

    # iteration
    for row in range(1, R):
        for col in range(1, C):
            sR = F[row - 1][col] + pen
            sD = F[row - 1][col - 1] + mx_sc[s1[col - 1] + s2[row - 1]]
            sC = F[row][col - 1] + pen
            sG = 0
            zippa = list(zip((sC, sR, sD, sG), ("l", "u", "d", "Z")))
            final = max(zippa)
            F[row][col], P[row][col] = final
    return F, P


def score_ali(F, P, seq1, seq2):
    # i have to start from highest score cell
    max = 0
    row = 0
    col = 0

    for r in range(len(F)):
        for c in range(len(F[0])):
            if max == 0 or F[r][c] > max:
                max = F[r][c]
                row = r
                col = c

    template = ''
    target = ''
    intra = ''
    score = F[row][col]

    while F[row][col] != 0:
        if P[row][col] == 'd':
            template += seq1[col - 1]
            target += seq2[row - 1]
            intra += '|'
            row -= 1
            col -= 1
        elif P[row][col] == 'l':
            template += seq1[col - 1]
            target += '-'
            intra += ' '
            col -= 1
        elif P[row][col] == 'u':
            template += '-'
            target += seq2[row - 1]
            intra += ' '
            row -= 1

    intra = intra[::-1]
    template = template[::-1]
    target = target[::-1]
    return template, target, intra, score


##############################################################################################################
# to get the input from the user:
# seq1_path = input('Please, insert path file: ')
# seq1_file = open('seq1_path', 'r')
# seq1 = ''
# for line in seq1_file:
#     line = line.rstrip()
#     seq1 += line
#------------------------------------------------------------------
# seq2_path = input('Please, insert path file: ')
# seq2_file = open('seq1_path', 'r')
# seq2_file = open('/home/fecke/PycharmProjects/programming_stefano_roncelli/data/titin_mo.txt', 'r')
# seq2 = ''
# for line in seq2_file:
#     line = line.rstrip()
#     seq2 += line
##############################################################################################################

seq1 = 'AAAAAAATTTAAAAAAAAA'
seq2 = 'ATA'
mx_file = open('../data/blosum.txt', 'r')
S = matrix_dict(mx_file)
print(S)
d = -2


f, p = score_trace(seq1, seq2, S, d)

s1, s2, intra, sc = score_ali(f, p, seq1, seq2)

for i in range(0, len(s1), 60):
    print('\n', s1[i: i+60], '\n', intra[i:i+60], "\n", s2[i:i+60])
print("\nWith a score of: ", sc)



#######################################################################################
# to print the matrices #
for k in range(len(f)):
    print (f[k])
# for z in range(len(p)):
#     print(p[z])
#######################################################################################