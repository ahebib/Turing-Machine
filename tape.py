#Programmer: Ammar Hebib
#tape.py
<<<<<<< HEAD
#Tape object used in Universal Turing Machine
=======
#Tape used in Universal Turing Machine
>>>>>>> 4994ecaa4660675371c1dffd19cef0a47db0529b

class Tape():
        tapeObj = []

<<<<<<< HEAD
        def stringToArray(self, tapeString):
            self.tapeObj = list(tapeString)

        def arrayToString(self):
            strTape = ''
            for i in range(len(self.tapeObj)):
                strTape = strTape + self.tapeObj[i]
            return strTape
            
        def extendRight(self):
            self.tapeObj.append('b')

        def extendLeft(self):
            self.tapeObj.insert(0,'b')

        def getValue(self,position):
            value = self.tapeObj[position]

            return value

        def setValue(self, position, replacement):
            self.tapeObj[position] = replacement

        def getTapeLength(self):
            return len(self.tapeObj)
=======
        def __init__(self, userInput):
            self.tapeObj = list(userInput)
            
        def extendRight(self):
            self.tapeObj.append('b')
>>>>>>> 4994ecaa4660675371c1dffd19cef0a47db0529b
