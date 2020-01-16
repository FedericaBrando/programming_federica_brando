

def dic_matrix(filepath):
    file_mx = open(filepath, "r")
    aminoacid = file_mx.readline().split()
    ami = aminoacid[3]
    m = {}

    for aa in ami:
        col = file_mx.readline().split()
        for i in range(len(col)):
            m[aa + ami[i]] = int(col[i][:-1])
    file_mx.close()
    return m


def dic_pen(dictionary, pen_value):
    aa = 'ARNDCQEGHILKMFPSTWYV'
    for am in aa:
        dictionary[am+'-'] = int(pen_value)
        dictionary['-'+am] = int(pen_value)
    return dictionary


def score_ali(seq1, seq2, score_dic): #the commented part is done for gap penalty extension
    score = 0
    # gap_penalty = -2
    # ext = 0
    # g_e = 0.5
    if len(seq1) == len(seq2):
        for aa1, aa2 in zip(seq1, seq2):
            # if aa1 == '-' or aa2 == '-':
            #     # ext += 1
            #     score += gap_penalty - (ext - 1) * g_e
            if aa1+aa2 in score_dic:
                # ext = 0
                score += score_dic[aa1+aa2]
            elif aa1+aa2 not in score_dic:
                # ext = 0
                score += score_dic[aa2+aa1]
            # elif aa1 == '-' or aa2 == '-':
            #     ext += 1
            #     score += gap_penalty - (ext - 1) * g_e
    else:
        print('sequences are not of the same alignment')
    return score


# 4) Read three alignments from the alignments.fasta file
def ali_score(file_path_ali, score_dic):
    ali_file_fasta = open(file_path_ali, 'r')
    ali = []

    for line in ali_file_fasta:
        if line[0] != '>':
            ali.append(line.rstrip())
    max_score = []
    if len(ali) % 2 == 0:  # checks that the alignments are paired
        for i in range(0, len(ali)-1, 2):
            score = score_ali(ali[i], ali[i+1], score_dic)
            print(ali[i], '\n', ali[i+1], '\n', score)
    else:  # if not it does not count the last one
        for i in range(0, len(ali) - 2, 2):
            score = score_ali(ali[i], ali[i + 1], score_dic)
            print('\n', ali[i], '\n', ali[i + 1], '\n', score)
    ali_file_fasta.close()
    return max_score

# 1) Read substitution matrices from the PAM250.txt and BLOSUM62.txt files.
# 2) Store substitution matrices in dictionaries.
# 5) Use the substitution matrices PAM250 and BLOSUM62 to score each alignment and compare the results.
#    For gap penalty use a linear gap model with d = -2.

# blosum_path = input('Insert BLOSUM scoring matrix file path: ')
blosum_path = 'BLOSUM62.txt'
pen = -2
# pen = input('insert penalty: ')
blosum_dic = dic_pen(dic_matrix(blosum_path), pen)
pam_path = 'PAM250.txt'
# pam_path = input('Insert PAM scoring matrix file path: ')
pam_dic = dic_pen(dic_matrix(pam_path), pen)

# 6) Print each alignment with its score

print('\nBLOSUM scores:')
blosum_score = ali_score('alignments.fasta', blosum_dic)
print('\nPAM scores:')
pam_score = ali_score('alignments.fasta', pam_dic)

