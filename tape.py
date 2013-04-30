#Programmer: Ammar Hebib
#tape.py
#Tape used in Universal Turing Machine

class Tape():
        tapeObj = []

        def __init__(self, userInput):
            self.tapeObj = list(userInput)
            
        def extendRight(self):
            self.tapeObj.append('b')
