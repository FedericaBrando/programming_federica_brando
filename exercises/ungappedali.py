##WARNING, this code is not perfect##


def score_ali(list1,list2,matrix_score):
	''' Function that computes the score between two sequences. Input values are: sequence one, sequence two, and the scoring matrix chosen '''
	score=0
	for base1,base2 in zip(list1,list2):	#scorre base1 e base 2 insieme lungo le sequenze
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


	listali=[]
	
	def reverse(seqA,seqB,listali):	
		''' Function that computes the best score between two sequences, it need an additional input where t'''
		matrix_score = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
        	        'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
        	        'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
        	        'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}
		score=0
	
		print(seqA)
		print(seqB)
		score=score_ali(seqA,seqB,matrix_score)
		print(score)
		align=[]
		align=[seqA , seqB, score]
		listali.append(align)
		#print(listali)
	
		if seqB[-1]!="-" and seqA[0]!="-":
			maximo=listali[0][2]
			for i in range(len(listali)):
				if listali[i][2] > maximo:

					maximo=listali[i][2]
					indice=i
					final=[listali[indice][0],listali[indice][1],maximo]

				elif listali[i][2] == maximo:
					otherali=[listali[i][0],listali[i][1]]
			

			print("the best ali is:\n", str(final[0]),"\n", str(final[1]), "\nand\n", str(otherali[0]),"\n", str(otherali[1]), "\nbest score: ", final[2])
			return 
			
		else:	
	
			if seqB[-1]=="-" and seqA[-1]!="-": #seqB è "-" e seqA è "lettera"

				seqB="-" + seqB[:-1]
				#print("elif1","\n", seqA,"\n",seqB)
				return reverse(seqA,seqB,listali)
				#return "\nSo far, so good"
		
			elif seqB[-1]!="-" and seqA[-1]!="-": #seqB è "lettera" e seqA è "lettera"

				seqB="-" + seqB
				seqA=seqA[1:]+"-"
				#print("elif2","\n", seqA,"\n",seqB)
						
				return reverse(seqA,seqB,listali)

			elif seqA[0]=="-" and seqB[0]=="-": #seqB è "lettera" e seqB è "-" 

				#seqB="-"+ seqB[:-1]
				seqA=seqA[1:]+"-"
				#print("elif3","\n", seqA,"\n",seqB)
				return reverse(seqA,seqB,listali)
			
 	
	return reverse(seqA,seqB,listali)
	
	
	
ali()


	


