def score_seq():
	seq1=input("seq1: ")
	seq2=input("seq2: ")
	score=0
	if len(seq1)!=len(seq2):
		print("le due sequenze non hanno la stessa lunghezza")
		score_seq()
	else:
		for i in range(len(seq1)):
			if seq1[i]!=seq2[i]:
				score=score+(-1)
			else:
				score=score+1
	return score

print(score_seq())
