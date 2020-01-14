score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}

def score_ali(list1,list2,matrix_score):
	score=0
	for base1,base2 in zip(list1,list2):
		if base1+base2 in matrix_score:
			score += matrix_score[base1+base2]
		else:
			score += 0
	print(score)


def reverse(seqA,seqB):
		
	matrix_score = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}
	
	print(seqA)
	print(seqB)

	if seqB[-1]=="-" and seqA[-1]!="-":
		score= score_ali(seqA,seqB,matrix_score)
		seqB="-" + seqB[:-1]
	
		reverse(seqA,seqB)

		return score

	elif seqB[-1]!="-" and seqA[-1]!="-":
		score= score_ali(seqA,seqB,matrix_score)
		seqB="-" + seqB[:-1]
		seqA=seqA+"-"
		
		reverse(seqA,seqB)		
		return score
	elif seqA[-1]=="-" and seqB[-1]!="-":
		score= score_ali(seqA,seqB,matrix_score)

		seqB="-"+ seqB[:-1]

		reverse(seqA,seqB)
		return score
		 
	else:
		score= score_ali(seqA,seqB,matrix_score)
		
		return score



		
	
seq1="ACTGTATAGATTTAG"
seq2="TTGTATTAG"

if len(seq1)>len(seq2):
	seqA=len(seq2)*"-"+seq1
	seqB=seq2+"-"*len(seq1)
else:
	seqA=len(seq1)*"-"+seq2
	seqB=seq1+"-"*len(seq2)

reverse(seqA,seqB)
	


