#!~/anaconda3/envs/PB/bin/python

# FINAL EXAM SCRIPT - FEDERICA BRANDO
#
# To build the Score and trace matrices, following Smith and Waterman algorithm:
#
# F(row,col), P(col, row)  = max{[F(row-1, col-1) + dict_score, "diag"]
#                               [F(row-1, col) + gap_penalty, "up"]
#                               [F(row, col-1) + gap_penalty, "left"]
#                               [0, "Z"]}
#

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
            aa = seq1[col - 1] + seq2[row - 1]
            sR = F[row - 1][col] + int(gap)
            sD = F[row - 1][col - 1] + dic[aa]
            sC = F[row][col - 1] + int(gap)
            sG = 0
            zippa = list(zip((sC, sR, sD, sG), ("l", "u", "d", "Z")))
            final = max(zippa)
            F[row][col], P[row][col] = final
    return F, P


def start_index(F):
    """Function that takes in input the score matrix, finds the highest scores throughout the whole matrix and
    stores into a list of tuples the indexes of the scores"""
    c = len(F[0])
    r = len(F)
    max_score = F[0][0]
    max_out = []
    for col in range(1, c):
        for row in range(1, r):
            temp_score = F[row][col]
            if temp_score > max_score:
                max_score = temp_score
                max_out = [[row, col]]
            elif temp_score == max_score:
                temp_coord = [row, col]
                max_out.append(temp_coord)
    return max_out


def sw_algo(F, P, seq1, seq2):
    """ b) Function that takes F, P, seq1 and seq2 as input and returns a list of tuples of the best local alignment(s)
    between seq1 and seq2 and the corresponding score(s)"""
    max_index = start_index(F)
    align = []

    for i in range(len(max_index)):
        row, col = max_index[i]
        score = F[row][col]
        template = ''
        target = ''
        intra = ''
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
        align += [[template[::-1], intra[::-1], target[::-1], score]]

    return align


if __name__ == "__main__":
    blosum50 = {'AA': 5.0, 'AR': -2.0, 'AN': -1.0, 'AD': -2.0, 'AC': -1.0, 'AQ': -1.0, 'AE': -1.0, 'AG': 0.0, 'AH': -2.0, 'AI': -1.0, 'AL': -2.0, 'AK': -1.0, 'AM': -1.0, 'AF': -3.0, 'AP': -1.0, 'AS': 1.0, 'AT': 0.0, 'AW': -3.0, 'AY': -2.0, 'AV': 0.0, 'RA': -2.0, 'RR': 7.0, 'RN': -1.0, 'RD': -2.0, 'RC': -4.0, 'RQ': 1.0, 'RE': 0.0, 'RG': -3.0, 'RH': 0.0, 'RI': -4.0, 'RL': -3.0, 'RK': 3.0, 'RM': -2.0, 'RF': -3.0, 'RP': -3.0, 'RS': -1.0, 'RT': -1.0, 'RW': -3.0, 'RY': -1.0, 'RV': -3.0, 'NA': -1.0, 'NR': -1.0, 'NN': 7.0, 'ND': 2.0, 'NC': -2.0, 'NQ': 0.0, 'NE': 0.0, 'NG': 0.0, 'NH': 1.0, 'NI': -3.0, 'NL': -4.0, 'NK': 0.0, 'NM': -2.0, 'NF': -4.0, 'NP': -2.0, 'NS': 1.0, 'NT': 0.0, 'NW': -4.0, 'NY': -2.0, 'NV': -3.0, 'DA': -2.0, 'DR': -2.0, 'DN': 2.0, 'DD': 8.0, 'DC': -4.0, 'DQ': 0.0, 'DE': 2.0, 'DG': -1.0, 'DH': -1.0, 'DI': -4.0, 'DL': -4.0, 'DK': -1.0, 'DM': -4.0, 'DF': -5.0, 'DP': -1.0, 'DS': 0.0, 'DT': -1.0, 'DW': -5.0, 'DY': -3.0, 'DV': -4.0, 'CA': -1.0, 'CR': -4.0, 'CN': -2.0, 'CD': -4.0, 'CC': 13.0, 'CQ': -3.0, 'CE': -3.0, 'CG': -3.0, 'CH': -3.0, 'CI': -2.0, 'CL': -2.0, 'CK': -3.0, 'CM': -2.0, 'CF': -2.0, 'CP': -4.0, 'CS': -1.0, 'CT': -1.0, 'CW': -5.0, 'CY': -3.0, 'CV': -1.0, 'QA': -1.0, 'QR': 1.0, 'QN': 0.0, 'QD': 0.0, 'QC': -3.0, 'QQ': 7.0, 'QE': 2.0, 'QG': -2.0, 'QH': 1.0, 'QI': -3.0, 'QL': -2.0, 'QK': 2.0, 'QM': 0.0, 'QF': -4.0, 'QP': -1.0, 'QS': 0.0, 'QT': -1.0, 'QW': -1.0, 'QY': -1.0, 'QV': -3.0, 'EA': -1.0, 'ER': 0.0, 'EN': 0.0, 'ED': 2.0, 'EC': -3.0, 'EQ': 2.0, 'EE': 6.0, 'EG': -3.0, 'EH': 0.0, 'EI': -4.0, 'EL': -3.0, 'EK': 1.0, 'EM': -2.0, 'EF': -3.0, 'EP': -1.0, 'ES': -1.0, 'ET': -1.0, 'EW': -3.0, 'EY': -2.0, 'EV': -3.0, 'GA': 0.0, 'GR': -3.0, 'GN': 0.0, 'GD': -1.0, 'GC': -3.0, 'GQ': -2.0, 'GE': -3.0, 'GG': 8.0, 'GH': -2.0, 'GI': -4.0, 'GL': -4.0, 'GK': -2.0, 'GM': -3.0, 'GF': -4.0, 'GP': -2.0, 'GS': 0.0, 'GT': -2.0, 'GW': -3.0, 'GY': -3.0, 'GV': -4.0, 'HA': -2.0, 'HR': 0.0, 'HN': 1.0, 'HD': -1.0, 'HC': -3.0, 'HQ': 1.0, 'HE': 0.0, 'HG': -2.0, 'HH': 10.0, 'HI': -4.0, 'HL': -3.0, 'HK': 0.0, 'HM': -1.0, 'HF': -1.0, 'HP': -2.0, 'HS': -1.0, 'HT': -2.0, 'HW': -3.0, 'HY': 2.0, 'HV': -4.0, 'IA': -1.0, 'IR': -4.0, 'IN': -3.0, 'ID': -4.0, 'IC': -2.0, 'IQ': -3.0, 'IE': -4.0, 'IG': -4.0, 'IH': -4.0, 'II': 5.0, 'IL': 2.0, 'IK': -3.0, 'IM': 2.0, 'IF': 0.0, 'IP': -3.0, 'IS': -3.0, 'IT': -1.0, 'IW': -3.0, 'IY': -1.0, 'IV': 4.0, 'LA': -2.0, 'LR': -3.0, 'LN': -4.0, 'LD': -4.0, 'LC': -2.0, 'LQ': -2.0, 'LE': -3.0, 'LG': -4.0, 'LH': -3.0, 'LI': 2.0, 'LL': 5.0, 'LK': -3.0, 'LM': 3.0, 'LF': 1.0, 'LP': -4.0, 'LS': -3.0, 'LT': -1.0, 'LW': -2.0, 'LY': -1.0, 'LV': 1.0, 'KA': -1.0, 'KR': 3.0, 'KN': 0.0, 'KD': -1.0, 'KC': -3.0, 'KQ': 2.0, 'KE': 1.0, 'KG': -2.0, 'KH': 0.0, 'KI': -3.0, 'KL': -3.0, 'KK': 6.0, 'KM': -2.0, 'KF': -4.0, 'KP': -1.0, 'KS': 0.0, 'KT': -1.0, 'KW': -3.0, 'KY': -2.0, 'KV': -3.0, 'MA': -1.0, 'MR': -2.0, 'MN': -2.0, 'MD': -4.0, 'MC': -2.0, 'MQ': 0.0, 'ME': -2.0, 'MG': -3.0, 'MH': -1.0, 'MI': 2.0, 'ML': 3.0, 'MK': -2.0, 'MM': 7.0, 'MF': 0.0, 'MP': -3.0, 'MS': -2.0, 'MT': -1.0, 'MW': -1.0, 'MY': 0.0, 'MV': 1.0, 'FA': -3.0, 'FR': -3.0, 'FN': -4.0, 'FD': -5.0, 'FC': -2.0, 'FQ': -4.0, 'FE': -3.0, 'FG': -4.0, 'FH': -1.0, 'FI': 0.0, 'FL': 1.0, 'FK': -4.0, 'FM': 0.0, 'FF': 8.0, 'FP': -4.0, 'FS': -3.0, 'FT': -2.0, 'FW': 1.0, 'FY': 4.0, 'FV': -1.0, 'PA': -1.0, 'PR': -3.0, 'PN': -2.0, 'PD': -1.0, 'PC': -4.0, 'PQ': -1.0, 'PE': -1.0, 'PG': -2.0, 'PH': -2.0, 'PI': -3.0, 'PL': -4.0, 'PK': -1.0, 'PM': -3.0, 'PF': -4.0, 'PP': 10.0, 'PS': -1.0, 'PT': -1.0, 'PW': -4.0, 'PY': -3.0, 'PV': -3.0, 'SA': 1.0, 'SR': -1.0, 'SN': 1.0, 'SD': 0.0, 'SC': -1.0, 'SQ': 0.0, 'SE': -1.0, 'SG': 0.0, 'SH': -1.0, 'SI': -3.0, 'SL': -3.0, 'SK': 0.0, 'SM': -2.0, 'SF': -3.0, 'SP': -1.0, 'SS': 5.0, 'ST': 2.0, 'SW': -4.0, 'SY': -2.0, 'SV': -2.0, 'TA': 0.0, 'TR': -1.0, 'TN': 0.0, 'TD': -1.0, 'TC': -1.0, 'TQ': -1.0, 'TE': -1.0, 'TG': -2.0, 'TH': -2.0, 'TI': -1.0, 'TL': -1.0, 'TK': -1.0, 'TM': -1.0, 'TF': -2.0, 'TP': -1.0, 'TS': 2.0, 'TT': 5.0, 'TW': -3.0, 'TY': -2.0, 'TV': 0.0, 'WA': -3.0, 'WR': -3.0, 'WN': -4.0, 'WD': -5.0, 'WC': -5.0, 'WQ': -1.0, 'WE': -3.0, 'WG': -3.0, 'WH': -3.0, 'WI': -3.0, 'WL': -2.0, 'WK': -3.0, 'WM': -1.0, 'WF': 1.0, 'WP': -4.0, 'WS': -4.0, 'WT': -3.0, 'WW': 15.0, 'WY': 2.0, 'WV': -3.0, 'YA': -2.0, 'YR': -1.0, 'YN': -2.0, 'YD': -3.0, 'YC': -3.0, 'YQ': -1.0, 'YE': -2.0, 'YG': -3.0, 'YH': 2.0, 'YI': -1.0, 'YL': -1.0, 'YK': -2.0, 'YM': 0.0, 'YF': 4.0, 'YP': -3.0, 'YS': -2.0, 'YT': -2.0, 'YW': 2.0, 'YY': 8.0, 'YV': -1.0, 'VA': 0.0, 'VR': -3.0, 'VN': -3.0, 'VD': -4.0, 'VC': -1.0, 'VQ': -3.0, 'VE': -3.0, 'VG': -4.0, 'VH': -4.0, 'VI': 4.0, 'VL': 1.0, 'VK': -3.0, 'VM': 1.0, 'VF': -1.0, 'VP': -3.0, 'VS': -2.0, 'VT': 0.0, 'VW': -3.0, 'VY': -1.0, 'VV': 5.0}

    s1 = sys.argv[1]
    s2 = sys.argv[2]
    gap = sys.argv[3]
    score, trace = sw_matrix(s1, s2, blosum50, gap)

    for l in score:
        print(l)
    for col in trace:
        print(col)

    final_align = sw_algo(score, trace, s1, s2)
    #  c) Print the alignment(s) and the corresponding score(s)
    for i in range(len(final_align)):
        print(final_align[i][0])
        print(final_align[i][1])
        print(final_align[i][2])
        print('Score:', final_align[i][3])
