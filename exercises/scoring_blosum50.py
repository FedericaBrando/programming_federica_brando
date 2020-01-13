
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
		blosum=[] 			#dichiara una variabile lista 
		for line in blosum50:		
			line=line.rstrip()	
			line=line.split()	
			#print(line)
			blosum.append(line)	#blosum è una lista di liste (tabella)
			
		blosumdict={}			#dichiara un dizionario vuoto
		for i in range(len(blosum[0])):	#for loop necessario per la prima iterazione nella tabella // va da o alla lunghezza della lista in posizione 0 di lista
			for j in range(1, len(blosum)): #for loop che va da 1 a lunghezza di blosum
				blosumdict[blosum[0][i]+blosum[j][0]]=blosum[i+1][j] #crea una key che è data dalla somma del valore della prima riga + il valore della prima colonna e il value associato è il valore del valore
		
		for base1,base2 in zip(seq1,seq2):
			score+=int(blosumdict[base1+base2])
					
	return score

print(score_blosum50())
