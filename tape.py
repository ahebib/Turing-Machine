#Programmer: Ammar Hebib
#tape.py
#Tape object used in Universal Turing Machine
#Tape used in Universal Turing Machine
#Tape used in Universal Turing Machine

class Tape():
        tapeObj = []


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

        def __init__(self, userInput):
            self.tapeObj = list(userInput)
            
        def extendRight(self):
            self.tapeObj.append('b')
