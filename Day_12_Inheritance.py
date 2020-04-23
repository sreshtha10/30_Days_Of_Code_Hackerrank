class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstname,lastname,idNum,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
    def  printPerson(self):
        print('Name: '+self.lastName+', '+self.firstName)
        print('ID: '+self.idNum)
    def calculate(self):
        avg = sum(listitem for listitem in self.scores)/len(self.scores)
        if(avg < 40):
            return 'T'
        elif(avg >= 40 and avg <55):
            return 'D'
        elif (avg >=55 and avg <70):
            return 'P'
        elif(avg >=70 and avg <80):
            return 'A'
        elif (avg >=80 and avg <90):
            return 'E'
        elif (avg >=90 and avg <=100):
            return 'O'
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
