####################################################################################################
# 4) Write a script that stores into a Python dictionary a substitution matrix in diagonal format. #
####################################################################################################
# ALSKLASPALSAKDLDSPAL    ALSKLA-SPALSAKDLDSPAL    ALSKLASPALSAKDLDSPA-L    ALSKLASPALSAKDLDSPA-LS #
# ALSKIADSLAPIKDLSPASL    ALSKIADSLAP-IKDLSPASL    ALSKIADSLAPIKDLS-PASL    ALSKIADSLAPIKDLS-PASLT #
#                                                                                                  #
#                  Which one gets the highest score using PAM250 and d = -1?                       #
#                 Which one gets the highest score using BLOSUM62 and d = -1?                      #
####################################################################################################

aa = 'ARNDCQEGHILKMFPSTWYV'

def scoring_dic(filepath):  # reads diagonal matrix and makes a dictionary
    sc_mx_file = open(filepath, 'r')
    sc_dict = {}
    for am in aa:
        line = sc_mx_file.readline().split()
        for i in range(len(line)):
            sc_dict[am+aa[i]] = int(line[i][:-1])

    sc_mx_file.close()
    return sc_dict

def add_pen(score_dic, penalty):  # adds penalty
    for ami in aa:
        score_dic[ami+'-'] = int(penalty)
        score_dic['-'+ami] = int(penalty)
    return score_dic

def scoring(scoring_mx, seq1, seq2):
    score = 0
    for aa1, aa2 in zip(seq1,seq2):
        if aa1+aa2 not in scoring_mx:
            score += scoring_mx[aa2+aa1]
        else:
            score += scoring_mx[aa1+aa2]
    return score

path = input('Insert scoring matrix file path: ')
# path = ../data/BLOSUM.txt
# path = ../data/PAM250.txt

pen = input('penalty: ')
# pen = -1

s_p = add_pen(scoring_dic(path), pen)

l =  ['ALSKLASPALSAKDLDSPAL', 'ALSKIADSLAPIKDLSPASL',
      'ALSKLA-SPALSAKDLDSPAL', 'ALSKIADSLAP-IKDLSPASL',
      'ALSKLASPALSAKDLDSPA-L', 'ALSKIADSLAPIKDLS-PASL',
      'ALSKLASPALSAKDLDSPA-LS', 'ALSKIADSLAPIKDLS-PASLT']

max_score = []
for i in range(0, len(l)-1, 2):
    final_score = scoring(s_p, l[i], l[i+1])
    if len(max_score) == 0 or final_score > max_score[0][2]:
        max_score = [(l[i], l[i+1], final_score)]
    elif max_score[0][2] == final_score:
        max_score.append((l[i], l[i+1], final_score))

if len(max_score) > 1:
    print('\nThe best alignments, are:')
    for i in range(len(max_score)):
        print('\n', max_score[i][0], '\n', max_score[i][1])
else:
    print('\nThe best alignment is:', '\n', max_score[0][0], '\n', max_score[0][1], '\n')

print('\nwith a score of: ', final_score, '\n')

