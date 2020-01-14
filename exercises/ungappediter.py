##################################
#   Ungapped iterative version   #
##################################


def score_ali(seq1, seq2, score_mtrx):

    score = 0
    for base1, base2 in zip(seq1, seq2):
        if base1 + base2 in score_mtrx:
            score += score_mtrx[base1+base2]
        elif (base1 == "-" and base2 != "-") or (base1 != "-" and base2 == "-"):
            score -= 2
    return score


def ali(score_matrix):
    seq1 = input("First sequence: ")
    seq2 = input("Second sequence: ")

    if len(seq1) > len(seq2):
        s1 = seq1 + (len(seq2) * '-')
        s2 = (len(seq1) * '-') + seq2
    else:
        s1 = (len(seq1) * '-') + seq2
        s2 = seq1+(len(seq2)*'-')

    max_tab = []

    while s1[-1] == '-' or s2[0] == '-':  # fin tanto che la seq1/seq2 ha come ultimo/primo char '-' entra in while

        score = score_ali(s1, s2, score_matrix)

        if len(max_tab) == 0 or score > max_tab[0][2]:
            max_tab = [(s1, s2, score)]
        elif score == max_tab[0][2]:
            max_tab.append((s1, s2, score))

        print(s1)
        print(s2)
        print(score)

        if s1[-1] == '-' and s2[0] == "-":  # se l'ultimo della s1 è '-' e il primo di s2 è "-"
            s1 = '-' + s1[:-1]
        elif s1[-1] != '-' and s2[0] == '-':  # se l'ultimo di s1 e di s2 non è '-'
            s2 = s2[1:] + '-'
    return max_tab


matrix_score = {'AA': 2, 'AC': -1, 'AT': -1, 'AG': 0, 'CA': -1,
                'CC': 2, 'CT': 0, 'CG': -1, 'TA': -1, 'TC': 0,
                'TT': 2, 'TG': -1, 'GA': 0, 'GC': -1, 'GT': -1, 'GG': 2}

max_ali = ali(matrix_score)

print("Best alignment is: ")
for i in range(len(max_ali)):
    print(max_ali[i][0])
    print(max_ali[i][1])
    print(max_ali[i][2])

