score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}

def score_ali(list1,list2,matrix_score):
	score=0
	for base1,base2 in zip(list1,list2):
		if base1+base2 in matrix_score:
			score += matrix_score[base1+base2]
	#		print("first",base1,base2)
		elif (base1=="-" and base2!="-") or (base1!="-" and base2=="-"):			
			score += -2
	#		print("elif",base1,base2)
		else:
			score+=0
	#		print("else",base1,base2)
		
	#	print(score)
	#print("the final score is ", score)
	return score


def reverse(seqA,seqB,listali):	
	matrix_score = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}
	score=0
	
	#print(seqA)
	#print(seqB)
	score=score_ali(seqA,seqB,matrix_score)
	#print(score)
	align=[]
	align=[seqA , seqB, score]
	listali.append(align)
	#print(listali)
	
	if seqB[-1]=="-" and seqA[-1]=="-":
		#print(seqA)
		#print(seqB)
		#print("if ",seqA, seqB) 
		#print(listali)
		maximo=listali[0][2]
		#print(maximo)
		for i in range(len(listali)):
			if listali[i][2] > maximo:
				#print(listali[i][2], maximo)
				maximo=listali[i][2]
				#print(maximo)
				indice=i
				#print(indice)
				final=[listali[indice][0],listali[indice][1],maximo]
		print("the best ali is:\n", str(final[0]), "\n", str(final[1]), "\n", "best score: ", final[2] )
		#return final
	else:	

		if seqB[-1]=="-" and seqA[-1]!="-":
			seqB="-" + seqB[:-1]
			#print("elif1", seqA,seqB)
			reverse(seqA,seqB,listali)
			return "\nciao"
	
		elif seqB[-1]!="-" and seqA[-1]!="-":
			seqB="-" + seqB[:-1]
			seqA=seqA+"-"
			#print("elif2", seqA,seqB)
			reverse(seqA,seqB,listali)		
			return 
		elif seqA[-1]=="-" and seqB[-1]!="-":
			seqB="-"+ seqB[:-1]
			#print("elif3", seqA,seqB)
			reverse(seqA,seqB,listali)
			return 
 

	
	
seq1=input("gimme the first sequence: ")
seq2=input("gimme the second sequence: ")

if len(seq1)>len(seq2):
	seqA=len(seq2)*"-"+seq1
	seqB=seq2+"-"*len(seq1)
else:
	seqA=len(seq1)*"-"+seq2
	seqB=seq1+"-"*len(seq2)


listali=[]

print(reverse(seqA,seqB,listali))


	


