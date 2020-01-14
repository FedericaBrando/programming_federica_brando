##WARNING, this code is not perfect##


def score_ali(list1,list2,matrix_score):
    ''' Function that computes the score between two sequences. Input values are: sequence one, sequence two, and the scoring matrix chosen '''
    score=0
    for base1,base2 in zip(list1,list2):            #scorre base1 e base 2 insieme lungo le sequenze
        if base1+base2 in matrix_score:
            score += matrix_score[base1+base2]
        elif (base1=="-" and base2!="-") or (base1!="-" and base2=="-"):            
            score -= 2
        
    return score

def ali():
    seq1=input("gimme the first sequence: ")
    seq2=input("gimme the second sequence: ")

    if len(seq1)>len(seq2):

        seqA=len(seq2)*"-"+seq1
        seqB=seq2+"-"*len(seq1)
    else:

        seqA=len(seq1)*"-"+seq2
        seqB=seq1+"-"*len(seq2)

    matrix_score = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                    'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                    'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                    'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}

    maxseqs = []
    
    while seqB[-1]=="-" or seqA[0]=="-":
        score=score_ali(seqA,seqB,matrix_score)
        if len(maxseqs) == 0 or score > maxseqs[0][2]:
            maxseqs=[(seqA , seqB, score)]
        elif score == maxseqs[0][2]:
            maxseqs.append((seqA , seqB, score))
        
        if seqB[-1]=="-" and seqA[-1]!="-": #seqB è "-" e seqA è "lettera"
            seqB="-" + seqB[:-1]
        elif seqB[-1]!="-" and seqA[-1]!="-": #seqB è "lettera" e seqA è "lettera"
            seqB="-" + seqB
            seqA=seqA[1:]+"-"
        elif seqA[0]=="-" and seqB[0]=="-": #seqB è "lettera" e seqB è "-"
            seqA=seqA[1:]+"-"
    
    print("\nbest alignments:\n")
    for maxseq in maxseqs:
        print(str(maxseq[0]) + "\n" + str(maxseq[1]),"\n")
    print("\nbest score: ", maxseqs[0][2])

ali()
