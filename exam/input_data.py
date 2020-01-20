
align1_sw_id = ['HBA_HUMA','HBB_HUMAN']
align2_sw_id = ['HBA_HUMA','LGB2_LUPLU']
align3_sw_id = ['HBA_HUMA','GST7_CAEEL']

align1 = ['GSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKL','GNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKL']
align2 = ['GSAQVKGHGKKVADALTNAVAHV---D--DMPNALSALSDLHAHKL','NNPELQAHAGKVFKLVYEAAIQLQVTGVVVTDATLKNLGSVHVSKG']
align3 = ['GSAQVKGHGKKVADALTNAVAHVDDMPNALSALS----DLHAHKL','GSGYLVGDSLTFVDL--LVAQHTADLLAANAALLDEFPQFKAHQE']

alignments = [align1, align2, align3]

matrix_rows_cols = 'ARNDCQEGHILKMFPSTWYV'

PAM250 = [[2.0], [-2.0, 6.0], [0.0, 0.0, 2.0], [0.0, -1.0, 2.0, 4.0], [-2.0, -4.0, -4.0, -5.0, 12.0], [0.0, 1.0, 1.0, 2.0, -5.0, 4.0], [0.0, -1.0, 1.0, 3.0, -5.0, 2.0, 4.0], [1.0, -3.0, 0.0, 1.0, -3.0, -1.0, 0.0, 5.0], [-1.0, 2.0, 2.0, 1.0, -3.0, 3.0, 1.0, -2.0, 6.0], [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -3.0, -2.0, 5.0], [-2.0, -3.0, -3.0, -4.0, -6.0, -2.0, -3.0, -4.0, -2.0, 2.0, 6.0], [-1.0, 3.0, 1.0, 0.0, -5.0, 1.0, 0.0, -2.0, 0.0, -2.0, -3.0, 5.0], [-1.0, 0.0, -2.0, -3.0, -5.0, -1.0, -2.0, -3.0, -2.0, 2.0, 4.0, 0.0, 6.0], [-4.0, -4.0, -4.0, -6.0, -4.0, -5.0, -5.0, -5.0, -2.0, 1.0, 2.0, -5.0, 0.0, 9.0], [1.0, 0.0, -1.0, -1.0, -3.0, 0.0, -1.0, -1.0, 0.0, -2.0, -3.0, -1.0, -2.0, -5.0, 6.0], [1.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 1.0, -1.0, -1.0, -3.0, 0.0, -2.0, -3.0, 1.0, 2.0], [1.0, -1.0, 0.0, 0.0, -2.0, -1.0, 0.0, 0.0, -1.0, 0.0, -2.0, 0.0, -1.0, -3.0, 0.0, 1.0, 3.0], [-6.0, 2.0, -4.0, -7.0, -8.0, -5.0, -7.0, -7.0, -3.0, -5.0, -2.0, -3.0, -4.0, 0.0, -6.0, -2.0, -5.0, 17.0], [-3.0, -4.0, -2.0, -4.0, 0.0, -4.0, -4.0, -5.0, 0.0, -1.0, -1.0, -4.0, -2.0, 7.0, -5.0, -3.0, -3.0, 0.0, 10.0], [0.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0, -2.0, 4.0, 2.0, -2.0, 2.0, -1.0, -1.0, -1.0, 0.0, -6.0, -2.0, 4.0]]

PAM250_dict = {'AA': 2.0, 'AR': -2.0, 'AN': 0.0, 'AD': 0.0, 'AC': -2.0, 'AQ': 0.0, 'AE': 0.0, 'AG': 1.0, 'AH': -1.0, 'AI': -1.0, 'AL': -2.0, 'AK': -1.0, 'AM': -1.0, 'AF': -4.0, 'AP': 1.0, 'AS': 1.0, 'AT': 1.0, 'AW': -6.0, 'AY': -3.0, 'AV': 0.0, 'RA': -2.0, 'RR': 6.0, 'RN': 0.0, 'RD': -1.0, 'RC': -4.0, 'RQ': 1.0, 'RE': -1.0, 'RG': -3.0, 'RH': 2.0, 'RI': -2.0, 'RL': -3.0, 'RK': 3.0, 'RM': 0.0, 'RF': -4.0, 'RP': 0.0, 'RS': 0.0, 'RT': -1.0, 'RW': 2.0, 'RY': -4.0, 'RV': -2.0, 'NA': 0.0, 'NR': 0.0, 'NN': 2.0, 'ND': 2.0, 'NC': -4.0, 'NQ': 1.0, 'NE': 1.0, 'NG': 0.0, 'NH': 2.0, 'NI': -2.0, 'NL': -3.0, 'NK': 1.0, 'NM': -2.0, 'NF': -4.0, 'NP': -1.0, 'NS': 1.0, 'NT': 0.0, 'NW': -4.0, 'NY': -2.0, 'NV': -2.0, 'DA': 0.0, 'DR': -1.0, 'DN': 2.0, 'DD': 4.0, 'DC': -5.0, 'DQ': 2.0, 'DE': 3.0, 'DG': 1.0, 'DH': 1.0, 'DI': -2.0, 'DL': -4.0, 'DK': 0.0, 'DM': -3.0, 'DF': -6.0, 'DP': -1.0, 'DS': 0.0, 'DT': 0.0, 'DW': -7.0, 'DY': -4.0, 'DV': -2.0, 'CA': -2.0, 'CR': -4.0, 'CN': -4.0, 'CD': -5.0, 'CC': 12.0, 'CQ': -5.0, 'CE': -5.0, 'CG': -3.0, 'CH': -3.0, 'CI': -2.0, 'CL': -6.0, 'CK': -5.0, 'CM': -5.0, 'CF': -4.0, 'CP': -3.0, 'CS': 0.0, 'CT': -2.0, 'CW': -8.0, 'CY': 0.0, 'CV': -2.0, 'QA': 0.0, 'QR': 1.0, 'QN': 1.0, 'QD': 2.0, 'QC': -5.0, 'QQ': 4.0, 'QE': 2.0, 'QG': -1.0, 'QH': 3.0, 'QI': -2.0, 'QL': -2.0, 'QK': 1.0, 'QM': -1.0, 'QF': -5.0, 'QP': 0.0, 'QS': -1.0, 'QT': -1.0, 'QW': -5.0, 'QY': -4.0, 'QV': -2.0, 'EA': 0.0, 'ER': -1.0, 'EN': 1.0, 'ED': 3.0, 'EC': -5.0, 'EQ': 2.0, 'EE': 4.0, 'EG': 0.0, 'EH': 1.0, 'EI': -2.0, 'EL': -3.0, 'EK': 0.0, 'EM': -2.0, 'EF': -5.0, 'EP': -1.0, 'ES': 0.0, 'ET': 0.0, 'EW': -7.0, 'EY': -4.0, 'EV': -2.0, 'GA': 1.0, 'GR': -3.0, 'GN': 0.0, 'GD': 1.0, 'GC': -3.0, 'GQ': -1.0, 'GE': 0.0, 'GG': 5.0, 'GH': -2.0, 'GI': -3.0, 'GL': -4.0, 'GK': -2.0, 'GM': -3.0, 'GF': -5.0, 'GP': -1.0, 'GS': 1.0, 'GT': 0.0, 'GW': -7.0, 'GY': -5.0, 'GV': -1.0, 'HA': -1.0, 'HR': 2.0, 'HN': 2.0, 'HD': 1.0, 'HC': -3.0, 'HQ': 3.0, 'HE': 1.0, 'HG': -2.0, 'HH': 6.0, 'HI': -2.0, 'HL': -2.0, 'HK': 0.0, 'HM': -2.0, 'HF': -2.0, 'HP': 0.0, 'HS': -1.0, 'HT': -1.0, 'HW': -3.0, 'HY': 0.0, 'HV': -2.0, 'IA': -1.0, 'IR': -2.0, 'IN': -2.0, 'ID': -2.0, 'IC': -2.0, 'IQ': -2.0, 'IE': -2.0, 'IG': -3.0, 'IH': -2.0, 'II': 5.0, 'IL': 2.0, 'IK': -2.0, 'IM': 2.0, 'IF': 1.0, 'IP': -2.0, 'IS': -1.0, 'IT': 0.0, 'IW': -5.0, 'IY': -1.0, 'IV': 4.0, 'LA': -2.0, 'LR': -3.0, 'LN': -3.0, 'LD': -4.0, 'LC': -6.0, 'LQ': -2.0, 'LE': -3.0, 'LG': -4.0, 'LH': -2.0, 'LI': 2.0, 'LL': 6.0, 'LK': -3.0, 'LM': 4.0, 'LF': 2.0, 'LP': -3.0, 'LS': -3.0, 'LT': -2.0, 'LW': -2.0, 'LY': -1.0, 'LV': 2.0, 'KA': -1.0, 'KR': 3.0, 'KN': 1.0, 'KD': 0.0, 'KC': -5.0, 'KQ': 1.0, 'KE': 0.0, 'KG': -2.0, 'KH': 0.0, 'KI': -2.0, 'KL': -3.0, 'KK': 5.0, 'KM': 0.0, 'KF': -5.0, 'KP': -1.0, 'KS': 0.0, 'KT': 0.0, 'KW': -3.0, 'KY': -4.0, 'KV': -2.0, 'MA': -1.0, 'MR': 0.0, 'MN': -2.0, 'MD': -3.0, 'MC': -5.0, 'MQ': -1.0, 'ME': -2.0, 'MG': -3.0, 'MH': -2.0, 'MI': 2.0, 'ML': 4.0, 'MK': 0.0, 'MM': 6.0, 'MF': 0.0, 'MP': -2.0, 'MS': -2.0, 'MT': -1.0, 'MW': -4.0, 'MY': -2.0, 'MV': 2.0, 'FA': -4.0, 'FR': -4.0, 'FN': -4.0, 'FD': -6.0, 'FC': -4.0, 'FQ': -5.0, 'FE': -5.0, 'FG': -5.0, 'FH': -2.0, 'FI': 1.0, 'FL': 2.0, 'FK': -5.0, 'FM': 0.0, 'FF': 9.0, 'FP': -5.0, 'FS': -3.0, 'FT': -3.0, 'FW': 0.0, 'FY': 7.0, 'FV': -1.0, 'PA': 1.0, 'PR': 0.0, 'PN': -1.0, 'PD': -1.0, 'PC': -3.0, 'PQ': 0.0, 'PE': -1.0, 'PG': -1.0, 'PH': 0.0, 'PI': -2.0, 'PL': -3.0, 'PK': -1.0, 'PM': -2.0, 'PF': -5.0, 'PP': 6.0, 'PS': 1.0, 'PT': 0.0, 'PW': -6.0, 'PY': -5.0, 'PV': -1.0, 'SA': 1.0, 'SR': 0.0, 'SN': 1.0, 'SD': 0.0, 'SC': 0.0, 'SQ': -1.0, 'SE': 0.0, 'SG': 1.0, 'SH': -1.0, 'SI': -1.0, 'SL': -3.0, 'SK': 0.0, 'SM': -2.0, 'SF': -3.0, 'SP': 1.0, 'SS': 2.0, 'ST': 1.0, 'SW': -2.0, 'SY': -3.0, 'SV': -1.0, 'TA': 1.0, 'TR': -1.0, 'TN': 0.0, 'TD': 0.0, 'TC': -2.0, 'TQ': -1.0, 'TE': 0.0, 'TG': 0.0, 'TH': -1.0, 'TI': 0.0, 'TL': -2.0, 'TK': 0.0, 'TM': -1.0, 'TF': -3.0, 'TP': 0.0, 'TS': 1.0, 'TT': 3.0, 'TW': -5.0, 'TY': -3.0, 'TV': 0.0, 'WA': -6.0, 'WR': 2.0, 'WN': -4.0, 'WD': -7.0, 'WC': -8.0, 'WQ': -5.0, 'WE': -7.0, 'WG': -7.0, 'WH': -3.0, 'WI': -5.0, 'WL': -2.0, 'WK': -3.0, 'WM': -4.0, 'WF': 0.0, 'WP': -6.0, 'WS': -2.0, 'WT': -5.0, 'WW': 17.0, 'WY': 0.0, 'WV': -6.0, 'YA': -3.0, 'YR': -4.0, 'YN': -2.0, 'YD': -4.0, 'YC': 0.0, 'YQ': -4.0, 'YE': -4.0, 'YG': -5.0, 'YH': 0.0, 'YI': -1.0, 'YL': -1.0, 'YK': -4.0, 'YM': -2.0, 'YF': 7.0, 'YP': -5.0, 'YS': -3.0, 'YT': -3.0, 'YW': 0.0, 'YY': 10.0, 'YV': -2.0, 'VA': 0.0, 'VR': -2.0, 'VN': -2.0, 'VD': -2.0, 'VC': -2.0, 'VQ': -2.0, 'VE': -2.0, 'VG': -1.0, 'VH': -2.0, 'VI': 4.0, 'VL': 2.0, 'VK': -2.0, 'VM': 2.0, 'VF': -1.0, 'VP': -1.0, 'VS': -1.0, 'VT': 0.0, 'VW': -6.0, 'VY': -2.0, 'VV': 4.0}

BLOSUM62 = [[6.0], [-2.0, 8.0], [-2.0, -1.0, 8.0], [-3.0, -2.0, 2.0, 9.0], [-1.0, -5.0, -4.0, -5.0, 13.0], [-1.0, 1.0, 0.0, 0.0, -4.0, 8.0], [-1.0, 0.0, 0.0, 2.0, -5.0, 3.0, 7.0], [0.0, -3.0, -1.0, -2.0, -4.0, -3.0, -3.0, 8.0], [-2.0, 0.0, 1.0, -2.0, -4.0, 1.0, 0.0, -3.0, 11.0], [-2.0, -4.0, -5.0, -5.0, -2.0, -4.0, -5.0, -6.0, -5.0, 6.0], [-2.0, -3.0, -5.0, -5.0, -2.0, -3.0, -4.0, -5.0, -4.0, 2.0, 6.0], [-1.0, 3.0, 0.0, -1.0, -5.0, 2.0, 1.0, -2.0, -1.0, -4.0, -4.0, 7.0], [-1.0, -2.0, -3.0, -5.0, -2.0, -1.0, -3.0, -4.0, -2.0, 2.0, 3.0, -2.0, 8.0], [-3.0, -4.0, -4.0, -5.0, -4.0, -5.0, -5.0, -5.0, -2.0, 0.0, 1.0, -5.0, 0.0, 9.0], [-1.0, -3.0, -3.0, -2.0, -4.0, -2.0, -2.0, -3.0, -3.0, -4.0, -4.0, -2.0, -4.0, -5.0, 11.0], [2.0, -1.0, 1.0, 0.0, -1.0, 0.0, 0.0, 0.0, -1.0, -4.0, -4.0, 0.0, -2.0, -4.0, -1.0, 6.0], [0.0, -2.0, 0.0, -2.0, -1.0, -1.0, -1.0, -2.0, -3.0, -1.0, -2.0, -1.0, -1.0, -3.0, -2.0, 2.0, 7.0], [-4.0, -4.0, -6.0, -6.0, -3.0, -3.0, -4.0, -4.0, -4.0, -4.0, -2.0, -4.0, -2.0, 1.0, -5.0, -4.0, -4.0, 16.0], [-3.0, -3.0, -3.0, -5.0, -4.0, -2.0, -3.0, -5.0, 3.0, -2.0, -2.0, -3.0, -1.0, 4.0, -4.0, -3.0, -2.0, 3.0, 10.0], [0.0, -4.0, -4.0, -5.0, -1.0, -3.0, -4.0, -5.0, -5.0, 4.0, 1.0, -3.0, 1.0, -1.0, -4.0, -2.0, 0.0, -4.0, -2.0, 6.0]]

BLOSUM62_dict = {'GW': -4.0, 'GV': -5.0, 'GT': -2.0, 'GS': 0.0, 'GR': -3.0, 'GQ': -3.0, 'GP': -3.0, 'GY': -5.0, 'GG': 8.0, 'GF': -5.0, 'GE': -3.0, 'GD': -2.0, 'GC': -4.0, 'GA': 0.0, 'GN': -1.0, 'GM': -4.0, 'GL': -5.0, 'GK': -2.0, 'GI': -6.0, 'GH': -3.0, 'ME': -3.0, 'MD': -5.0, 'MG': -4.0, 'MF': 0.0, 'MA': -1.0, 'MC': -2.0, 'MM': 8.0, 'ML': 3.0, 'MN': -3.0, 'MI': 2.0, 'MH': -2.0, 'MK': -2.0, 'MT': -1.0, 'MW': -2.0, 'MV': 1.0, 'MQ': -1.0, 'MP': -4.0, 'MS': -2.0, 'MR': -2.0, 'MY': -1.0, 'FP': -5.0, 'FQ': -5.0, 'FR': -4.0, 'FS': -4.0, 'FT': -3.0, 'FV': -1.0, 'FW': 1.0, 'FY': 4.0, 'FA': -3.0, 'FC': -4.0, 'FD': -5.0, 'FE': -5.0, 'FF': 9.0, 'FG': -5.0, 'FH': -2.0, 'FI': 0.0, 'FK': -5.0, 'FL': 1.0, 'FM': 0.0, 'FN': -4.0, 'SY': -3.0, 'SS': 6.0, 'SR': -1.0, 'SQ': 0.0, 'SP': -1.0, 'SW': -4.0, 'SV': -2.0, 'ST': 2.0, 'SK': 0.0, 'SI': -4.0, 'SH': -1.0, 'SN': 1.0, 'SM': -2.0, 'SL': -4.0, 'SC': -1.0, 'SA': 2.0, 'SG': 0.0, 'SF': -4.0, 'SE': 0.0, 'SD': 0.0, 'YI': -2.0, 'YH': 3.0, 'YK': -3.0, 'YM': -1.0, 'YL': -2.0, 'YN': -3.0, 'YA': -3.0, 'YC': -4.0, 'YE': -3.0, 'YD': -5.0, 'YG': -5.0, 'YF': 4.0, 'YY': 10.0, 'YQ': -2.0, 'YP': -4.0, 'YS': -3.0, 'YR': -3.0, 'YT': -2.0, 'YW': 3.0, 'YV': -2.0, 'LF': 1.0, 'LG': -5.0, 'LD': -5.0, 'LE': -4.0, 'LC': -2.0, 'LA': -2.0, 'LN': -5.0, 'LL': 6.0, 'LM': 3.0, 'LK': -4.0, 'LH': -4.0, 'LI': 2.0, 'LV': 1.0, 'LW': -2.0, 'LT': -2.0, 'LR': -3.0, 'LS': -4.0, 'LP': -4.0, 'LQ': -3.0, 'LY': -2.0, 'RT': -2.0, 'RV': -4.0, 'RW': -4.0, 'RP': -3.0, 'RQ': 1.0, 'RR': 8.0, 'RS': -1.0, 'RY': -3.0, 'RD': -2.0, 'RE': 0.0, 'RF': -4.0, 'RG': -3.0, 'RA': -2.0, 'RC': -5.0, 'RL': -3.0, 'RM': -2.0, 'RN': -1.0, 'RH': 0.0, 'RI': -4.0, 'RK': 3.0, 'VH': -5.0, 'VI': 4.0, 'EM': -3.0, 'EL': -4.0, 'EN': 0.0, 'EI': -5.0, 'EH': 0.0, 'EK': 1.0, 'EE': 7.0, 'ED': 2.0, 'EG': -3.0, 'EF': -5.0, 'EA': -1.0, 'EC': -5.0, 'VM': 1.0, 'EY': -3.0, 'VN': -4.0, 'ET': -1.0, 'EW': -4.0, 'EV': -4.0, 'EQ': 3.0, 'EP': -2.0, 'ES': 0.0, 'ER': 0.0, 'VP': -4.0, 'VQ': -3.0, 'VR': -4.0, 'VT': 0.0, 'VW': -4.0, 'KC': -5.0, 'KA': -1.0, 'KG': -2.0, 'KF': -5.0, 'KE': 1.0, 'KD': -1.0, 'KK': 7.0, 'KI': -4.0, 'KH': -1.0, 'KN': 0.0, 'KM': -2.0, 'KL': -4.0, 'KS': 0.0, 'KR': 3.0, 'KQ': 2.0, 'KP': -2.0, 'KW': -4.0, 'KV': -3.0, 'KT': -1.0, 'KY': -3.0, 'DN': 2.0, 'DL': -5.0, 'DM': -5.0, 'DK': -1.0, 'DH': -2.0, 'DI': -5.0, 'DF': -5.0, 'DG': -2.0, 'DD': 9.0, 'DE': 2.0, 'DC': -5.0, 'DA': -3.0, 'DY': -5.0, 'DV': -5.0, 'DW': -6.0, 'DT': -2.0, 'DR': -2.0, 'DS': 0.0, 'DP': -2.0, 'DQ': 0.0, 'QQ': 8.0, 'QP': -2.0, 'QS': 0.0, 'QR': 1.0, 'QT': -1.0, 'QW': -3.0, 'QV': -3.0, 'QY': -2.0, 'QA': -1.0, 'QC': -4.0, 'QE': 3.0, 'QD': 0.0, 'QG': -3.0, 'QF': -5.0, 'QI': -4.0, 'QH': 1.0, 'QK': 2.0, 'QM': -1.0, 'QL': -3.0, 'QN': 0.0, 'WG': -4.0, 'WF': 1.0, 'WE': -4.0, 'WD': -6.0, 'WC': -3.0, 'WA': -4.0, 'WN': -6.0, 'WM': -2.0, 'WL': -2.0, 'WK': -4.0, 'WI': -4.0, 'WH': -4.0, 'WW': 16.0, 'WV': -4.0, 'WT': -4.0, 'WS': -4.0, 'WR': -4.0, 'WQ': -3.0, 'WP': -5.0, 'WY': 3.0, 'PR': -3.0, 'PS': -1.0, 'PP': 11.0, 'PQ': -2.0, 'PV': -4.0, 'PW': -5.0, 'PT': -2.0, 'PY': -4.0, 'PC': -4.0, 'PA': -1.0, 'PF': -5.0, 'PG': -3.0, 'PD': -2.0, 'PE': -2.0, 'PK': -2.0, 'PH': -3.0, 'PI': -4.0, 'PN': -3.0, 'PL': -4.0, 'PM': -4.0, 'CK': -5.0, 'CI': -2.0, 'CH': -4.0, 'CN': -4.0, 'CM': -2.0, 'CL': -2.0, 'CC': 13.0, 'CA': -1.0, 'CG': -4.0, 'CF': -4.0, 'CE': -5.0, 'CD': -5.0, 'CY': -4.0, 'CS': -1.0, 'CR': -5.0, 'CQ': -4.0, 'CP': -4.0, 'CW': -3.0, 'CV': -1.0, 'CT': -1.0, 'IY': -2.0, 'VA': 0.0, 'VC': -1.0, 'VD': -5.0, 'VE': -4.0, 'VF': -1.0, 'VG': -5.0, 'IQ': -4.0, 'IP': -4.0, 'IS': -4.0, 'IR': -4.0, 'VL': 1.0, 'IT': -1.0, 'IW': -4.0, 'IV': 4.0, 'II': 6.0, 'IH': -5.0, 'IK': -4.0, 'VS': -2.0, 'IM': 2.0, 'IL': 2.0, 'VV': 6.0, 'IN': -5.0, 'IA': -2.0, 'VY': -2.0, 'IC': -2.0, 'IE': -5.0, 'ID': -5.0, 'IG': -6.0, 'IF': 0.0, 'HY': 3.0, 'HR': 0.0, 'HS': -1.0, 'HP': -3.0, 'HQ': 1.0, 'HV': -5.0, 'HW': -4.0, 'HT': -3.0, 'HK': -1.0, 'HH': 11.0, 'HI': -5.0, 'HN': 1.0, 'HL': -4.0, 'HM': -2.0, 'HC': -4.0, 'HA': -2.0, 'HF': -2.0, 'HG': -3.0, 'HD': -2.0, 'HE': 0.0, 'NH': 1.0, 'NI': -5.0, 'NK': 0.0, 'NL': -5.0, 'NM': -3.0, 'NN': 8.0, 'NA': -2.0, 'NC': -4.0, 'ND': 2.0, 'NE': 0.0, 'NF': -4.0, 'NG': -1.0, 'NY': -3.0, 'NP': -3.0, 'NQ': 0.0, 'NR': -1.0, 'NS': 1.0, 'NT': 0.0, 'NV': -4.0, 'NW': -6.0, 'TY': -2.0, 'TV': 0.0, 'TW': -4.0, 'TT': 7.0, 'TR': -2.0, 'TS': 2.0, 'TP': -2.0, 'TQ': -1.0, 'TN': 0.0, 'TL': -2.0, 'TM': -1.0, 'TK': -1.0, 'TH': -3.0, 'TI': -1.0, 'TF': -3.0, 'TG': -2.0, 'TD': -2.0, 'TE': -1.0, 'TC': -1.0, 'TA': 0.0, 'AA': 6.0, 'AC': -1.0, 'AE': -1.0, 'AD': -3.0, 'AG': 0.0, 'AF': -3.0, 'AI': -2.0, 'AH': -2.0, 'AK': -1.0, 'AM': -1.0, 'AL': -2.0, 'AN': -2.0, 'AQ': -1.0, 'AP': -1.0, 'AS': 2.0, 'AR': -2.0, 'AT': 0.0, 'AW': -4.0, 'AV': 0.0, 'AY': -3.0, 'VK': -3.0}