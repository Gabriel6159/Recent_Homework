import random
import statistics
import csv

#Coin Flipper And Checker
def coinFlip(n):
	flipList=[]
	for i in range(0,n):
		flipList.append(random.randint(0,1))
	return flipList
def checkFlips(checkListFlip):
	sumHeads=0
	sumTails=0
	for item in checkListFlip:
		if item==1:
			sumHeads+=1
		else:
			sumTails+=1
	if sumHeads/sumTails>1.1 or sumTails/sumHeads>1.1:
		return('Non equivelant flips')
	else:
		return('Evenly distributed flips')
checkListFlip=coinFlip(1000)
#print(checkFlips(checkListFlips))

#Dice Roller And Checker
def dieRoll(n):	#Returns list
	rollList=[]
	for i in range(0,n):
		rollList.append(random.randint(1,6))
	return rollList
def checkRolls(checkListDice):
	numList=[1,2,3,4,5,6]
	val1=val2=val3=val4=val5=val6=0
	rollValList=[val1,val2,val3,val4,val5,val6]
	for roll in checkListDice:
		for x in range(0,len(numList)):
			if roll==numList[x]:
				rollValList[x]+=1
	for i in range(0,len(rollValList)):
		rollValList[i]/=1000
	print(rollValList)
	stdevRolls=statistics.stdev(rollValList)
	print(stdevRolls)
	if stdevRolls<0.013:
		return('Even distribution')
	else: 
		return('Uneven distribution')
dieRollCount=1000
checkListDice=dieRoll(dieRollCount)
#print(checkRolls(checkListDice))

#Divisor calc
def getDivisors(n):
	for i in range(2,n):
		if n%i==0:
			print(i)
#getDivisors(100)

#Prime Factorization
def isPrime(n):	#Stole this from interwebs
  for i in range(2,n):
    if n%i==0:
      return False
  return True
def primeFactor(n):	#Returns list
	primeList=[]
	for i in range(2,n):
		if n%i==0 and isPrime(i)==True:
			primeList.append(i)
	return primeList
#print(primeFactor(100))

#Prime List
def isPrime(n):	#Stole this from interwebs
  for i in range(2,n):
    if n%i==0:
      return False
  return True
def primeNums(n):
	primeList=[]
	for i in range(2,n):
		if isPrime(i)==True:
			primeList.append(i)
	return primeList
#print(primeNums(100))

#Excel file
def getDivisorsFull(n):
	divisorListExcel=[]
	for i in range(1,n+1):
		if n%i==0:
			divisorListExcel.append(i)
	return divisorListExcel
def excelFactors(n):
	with open('factors.csv', 'w', newline='') as csvfile:
		factorwriter = csv.writer(csvfile, dialect='excel')
		for i in range (1,n+1):
			factorwriter.writerow(getDivisorsFull(i))
#excelFactors(24)

#GCD and LCM Calculator
def GCD(a,b):
	largest=0
	if a>b:
		largest=a
	else:
		largest=b
	for i in range(largest,1,-1):
		if a%i==0 and b%i==0:
			return i
		else:
			noDivisor=1
	return noDivisor
def LCM(a,b):
	largest=0
	if a>b:
		largest=a
	else:
		largest=b
	for i in range(largest,largest**3):
		if i%a==0 and i%b==0:
			return i
#print(GCD(144,256))
#print(LCM(144,256))

#Cart Class
class ShoppingCart:
	def __init__(self,itemList=[],itemCount=0):	#should
		self.itemList=itemList
		self.itemCount=itemCount
	def getItemList(self):
		return self.itemList
	def getItemCount(self):
		return self.itemCount
	def addItem(self,newItem):
		self.itemList.append(newItem)
		self.itemList.sort()
		self.itemCount+=1
		return 'Done'
	def __add__(self,newCart):
		newList=self.itemList+newCart.itemList
		newList.sort()
		newCount=self.itemCount+newCart.itemCount
		return ShoppingCart(newList,newCount)
	def __str__(self):
		return str(self.itemList)
cart1=ShoppingCart(['Pizza','Soda','Apples'],3)
cart2=ShoppingCart(['Bananas','Cashews','Bread','Beans'],4)
cart3=cart1+cart2
#print(cart3)
#print(cart3.itemCount)

#Fraction class
class Fraction:
	def __init__(self,a,b):	#numerator,denominator
		self.a=a
		self.b=b
	def simplify(self):
		commonNum=GCD(self.a,self.b)
		newNumer=self.a//commonNum
		newDenom=self.b//commonNum
		return Fraction(newNumer,newDenom)
	def __str__(self):
		return str(self.a)+'/'+str(self.b)
	def __add__(self,newFrac):
		numer1=self.a*newFrac.b
		numer2=self.b*newFrac.a
		denom=self.b*newFrac.b
		finalFrac=Fraction(numer1+numer2,denom)
		return finalFrac.simplify()
	def __sub__(self,newFrac):
		numer1=self.a*newFrac.b
		numer2=self.b*newFrac.a
		denom=self.b*newFrac.b
		finalFrac=Fraction(numer1-numer2,denom)
		return finalFrac.simplify()
	def __mul__(self,newFrac):
		frac3a=self.a*newFrac.a
		frac3b=self.b*newFrac.b
		finalFrac=Fraction(frac3a,frac3b)
		return finalFrac.simplify()
	def __floordiv__(self,newFrac):	#lazy divide
		frac3a=self.a*newFrac.b
		frac3b=self.b*newFrac.a
		finalFrac=Fraction(frac3a,frac3b)
		return finalFrac.simplify()
	def __truediv__(self,newFrac):
		frac3a=self.a*newFrac.b
		frac3b=self.b*newFrac.a
		finalFrac=Fraction(frac3a,frac3b)
		return finalFrac.simplify()
	def __lt__(self,frac2):	#less than
		frac1=self.simplify()
		frac2=self.simplify()
		if frac1.a/frac1.b<frac2.a/frac2.b:
			return True
		else:
			return False
	def __gt__(self,frac2):	#greater than
		frac1=self.simplify()
		frac2=self.simplify()
		if frac1.a/frac1.b>frac2.a/frac2.b:
			return True
		else: 
			return False
	def __le__(self,frac2):	#less than or equal to
		frac1=self.simplify()
		frac2=self.simplify()
		if frac1.a/frac1.b<=frac2.a/frac2.b:
			return True
		else:
			return False
	def __ge__(self,frac2):	#greater than or equal
		frac1=self.simplify()
		frac2=self.simplify()
		if frac1.a/frac1.b>=frac2.a/frac2.b:
			return True
		else: 
			return False
	def __eq__(self,frac2):	#equal to
		frac1=self.simplify()
		frac2=self.simplify()
		if frac1.a/frac1.b==frac2.a/frac2.b:
			return True
		else: 
			return False
frac1=Fraction(8,9)
frac2=Fraction(3,5)
print(frac1+frac2)
print(frac1-frac2)
print(frac1*frac2)
print(frac1/frac2)
fracUnsimp=Fraction(2,4)
print(fracUnsimp.simplify())
frac9=Fraction(1,2)
print(frac9.simplify())
