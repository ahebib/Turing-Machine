#Programmer: Ammar Hebib
#tape.py
#Tape object used in Universal Turing Machine

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
            #extends tape to the right
            self.tapeObj.append('b')

        def extendLeft(self):
            #extends tape to the left
            self.tapeObj.insert(0,'b')

        def getValue(self,position):
            value = self.tapeObj[position]

            return value

        def setValue(self, position, replacement):
            self.tapeObj[position] = replacement

        def getTapeLength(self):
            return len(self.tapeObj)
