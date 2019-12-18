####################################################
# How to find the RMSD after structure alignment.  #
# Write a script that can implement the root mean  #
# square deviation between the Ca of the residue   #
# of the first structure and the Ca of the residue #
# of the second structure, given a pdb file with   #
# both models                                      #  
####################################################

#rmsd=sqrt(1/n(sum from 1 to n [(x1-x2)^2+(y1-y2)^2+(z1-z2)^2])

from math import *
	
def rmsd_calc(coords1,coords2):
	sommatoria=0
	for i in range(len(coords1)):
		xcoords= float(coords1[i][0]) - float(coords2[i][0])
		ycoords= float(coords1[i][1])- float(coords2[i][1])
		zcoords= float(coords1[i][2])- float(coords2[i][2])
		sommatoria = sommatoria + (xcoords**2+ycoords**2+zcoords**2)
	rmsd=sqrt((1/len(coords1))*sommatoria)
	return rmsd
		
	
	

myfilepath=input("Please, insert the filepath of the pdb file aligned: ")

myfile=open(myfilepath,"r")	#apre il file dato in input
coords=[]			#crea lista vuota dove appendere sottoliste di coordinate
residue=[]			#crea lista vuota delle coords di ogni residuo
for line in myfile:
	#print(line)
	if line.startswith("ATOM") and "CA" in line: #entra nell'if solo se la riga inizia con ATOM e contiene il carbonio alfa
		linefile=line.rstrip()	
		coordsstr=linefile[32:55]	#assegna ad una stringa le tre coordinate
		residue=coordsstr.split()	#creo sottolista con le coords
		coords.append(residue)		#appendo ad una liste la sottolista

coords1=coords[:len(coords)//2] #divido in due liste le coordinate da confrontare
coords2=coords[len(coords)//2:]
			
print(rmsd_calc(coords1,coords2))

myfile.close()
