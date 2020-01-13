#######################################################
# Find the scoring matrix of the following alignment  #
#		ACAGGTGGACCT CTATATGG		      #
#		ACTGGTCGACTT CCGGATCG   	      #
#######################################################

seq1="ACAGGTGGACCTCTATATGG"
seq2="ACTGGTCGACTTCCGGATCG"


def prob_base(seq1,seq2,base):
	seq=seq1+seq2
	num_base=seq.count(base)
	prob=num_base/len(seq)
	return prob

def reverse(s):
	fs= s[::-1]
	return fs

def prob_matches(seq1,seq2):
	ali={ 	"AA":0, "CC":0, "AT":0, "GG":0, "TT":0, 
		"GC":0, "CT":0, "AG":0, "TG":0, "AC":0}
	for base1, base2 in zip(seq1, seq2):
		pair=base1+base2
		if pair in ali:
			ali[pair]+=1
		elif reverse(pair) in ali:
			ali[reverse(pair)]+=1
	for bp in ali:
		ali[bp]= ali[bp]/len(seq1)
	
	return ali
	
	
print(prob_matches(seq1,seq2))




