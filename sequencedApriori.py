from collections import defaultdict

def generateSet(a,b):
	#This function takes  in two lists; 
	#a, which is supposed to be the larger of the two lists
	#b, which is supposed to the be the single item list
	newList = []

	for item in a:
		for element in b:
			if element == item: #gets rid of initial single set vs single set duplicates
				continue
			else:	
				if hasDuplicate(item+element):
					continue
				else:
					if item+element not in newList:
						newList.append(item+element)



	return newList

def hasDuplicate(ourList):
	checkFreq = {}
	for item in ourList:
		if item in checkFreq.keys():
			checkFreq[item] +=1
		else:
			checkFreq[item] = 1
		if checkFreq[item] > 1:
			return True
	return False			

def checkSequence(seq,trans):
	#We will convert both the candidate sequence and the transaction into strings for the sake of comparison
	seqMap = map(str,seq)
	transMap = map(str,trans)
	seqString = ''.join(seqMap)
	transString = ''.join(transMap)
	if seqString in transString:
		return True
	else:
		return False

aprioriFile = open("tdb.txt","r") 

tdb = []

# Create the transaction database 
for line in aprioriFile :
	lineCharArray = line.strip('\n').split(',')
	lineArray = []
	for element in lineCharArray :
		lineArray.append(int(element))
	
	tdb.append(lineArray)

print("THIS IS THE TRANSACTION DATABASE: ")
print(tdb)
print()

k=1
n=2

freqMap = {}
F =defaultdict(list)

for transaction in tdb:
	for element in transaction:
		if element in freqMap.keys():
			freqMap[element] += 1
		else:
			freqMap[element] = 1
			
print("THIS IS THE FREQUENCY MAP: ")
print(freqMap)
print()

for element in freqMap:
	if freqMap[element] >= n:
		F[1].append([element])

print("THIS IS THE SINGLE ITEMSET LIST: ")
print(F[1])
print()

while len(F[k]) != 0:
	candidateSet = generateSet(F[k],F[1])

	for element in candidateSet:
		count = 0
		for transaction in tdb:
			hasSequence = checkSequence(element,transaction)
			if hasSequence == True:
				count += 1
			if count >= n:
				if element not in F[k+1]:
					F[k+1].append(element)

	k = k+1



print("THIS IS THE FINAL SET OF ITEMS THAT MEET MINIMUM SUPPORT:")
print(F)

	
