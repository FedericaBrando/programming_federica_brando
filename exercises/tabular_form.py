# 1) Write a function that multiplies two N*N matrices.
# As a test you can use:
#     A = [[2,4],
#          [3,1]]
#     B = [[2,1],
#          [1,3]]
#
# the result of which is:
#
# AB = [[8, 14]
#       [7, 6]]


def input_matrices():
    matrix1 = []
    matrix2 = []
    s1 = input("Write the first matrix separated by a comma (i.e: 1,2,3,4): ")
    s2 = input("Write the second matrix as stated before: ")

    mx1 = s1.split(',')
    mx2 = s2.split(',')

    if len(mx1) != 4 and len(mx2) != 4:

        print('matrices have to be 4x4 !!')
    else:

        for i in range(len(mx1)):
            mx1[i] = int(mx1[i])
            mx2[i] = int(mx2[i])

        i = 0
        while i < len(mx1):  # fin tanto che i è minore della lunghezza della matrice
            matrix1.append(mx1[i:i + 2])
            matrix2.append(mx2[i:i + 2])
            i += 2

    return matrix2, matrix1


def mult_matrices(m1, m2):
    m3 = []
    for i in range(len(m1)):  # per i che va da 0 a 2
        tab_ris = []
        for j in range(len(m1)):  # per j che va da 0 a 2
            ris = m1[i][0] * m2[0][j] + m1[i][1] * m2[1][j]
            tab_ris.append(ris)
        m3.append(tab_ris)
    return m3


mx1, mx2 = input_matrices()

print(mult_matrices(mx1, mx2))
