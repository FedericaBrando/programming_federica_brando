
def int_list(l):
	for i in range(len(l)):
		l[i]=int(l[i])
	return l

def score_blosum50():
	seq1=input("seq1: ")
	seq2=input("seq2: ")
	score=0
	blosum50=open("../data/blosum.txt","r")
	if len(seq1)!=len(seq2):
		print("le due sequenze non hanno la stessa lunghezza")
		blosum50.close()
		score_blosum50()
	else:
		blosumdict={}
		blosum=[]
		aa=blosum50.readline()
		aa=aa.split()
		for line in blosum50:
			line=line.rstrip()
			line=line[2:].split()
			line=int_list(line)
			blosum.append(line)
					
		for res in aa:
			for res2 in aa:
				blosumdict[res+res2]=0

		for k in blosumdict:
			for j in range(len(blosum)):
				for i in range(len(blosum)):
					print(blosum[j][i])
					blosumdict.update(k = blosum[j][i])
		
		#for line in blosum:
		#	print(line)
		#	for score,i in zip(line, blosumdict):
		#		print(score)
		#		blosumdict[i]=score
				#blosumdict[i]=score

		#for i in blosumdict:
		#	blosumdict
				
				
	return blosumdict

print(score_blosum50())


