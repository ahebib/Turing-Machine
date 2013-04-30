#Programmer: Ammar Hebib
#utm.py
#Universal Turing Machine
#everytime tape moves in direction append a 'b' in that direction
#tape.append('b')
#tape.insert(0,'b')
#only if can't make tape class
from tape import Tape

def main():
    userInput = raw_input("Type in a combination of 1s,0s, and b in the following format(ex. 11010bb...etc)")
    tape = Tape(userInput)
    print tape.tapeObj
    #state = initState()
    #position = start()
    #function(tape, state, position)


def initState():
    #initiates state
    state = 'q0'

    return state

def start():
    #select the start location on tape
    position = 0

    return position

def halt(tape, position, state):
    #stops the program
    print tape
    #exit(0)

def moveL(position):
    #move position 1 to the left
    position = position - 1
    
    return position

def moveR(position):
    #move position 1 to the right
    position = position + 1

    return position

def read(tape, position):
    #reads value at position on tape
    value = tape[position]

    return value

def write(tape, position, replacement):
    #replaces value at position with replacement
    tape[position] = replacement

    return tape

def function(tape, state, position):
    #changes state and determines what to do next
    value = read(tape,position)
    #q0 state -----------------------------------------------
    if(value == '0' and state == 'q0'):
        replacement = 'b'
        tape = write(tape, position, replacement)
        position = moveR(position)
        #change state
        state = 'q1'
        #recall function with new state
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q0'):
        replacement = 'b'
        tape = write(tape, position, replacement)
        position = moveR(position)
        state = 'q5'
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q0'):
        halt(tape, position, state)
    #q1 state -----------------------------------------------
    elif(value == '0' and state == 'q1'):
        position = moveR(position)
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q1'):
        position = moveR(position)
        state = 'q2'
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q1'):
        halt(tape, position, state)
    #q2 state -----------------------------------------------
    elif(value == '0' and state == 'q2'):
        replacement = '1'
        tape = write(tape, position, replacement)
        position = moveL(position)
        state = 'q3'
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q2'):
        position = moveR(position)
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q2'):
        position = moveL(position)
        state = 'q4'
        print tape
        function(tape, state, position)
    #q3 state -----------------------------------------------
    elif(value == '0' and state == 'q3'):
        position = moveL(position)
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q3'):
        position = moveL(position)
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q3'):
        position = moveR(position)
        state = 'q0'
        print tape
        function(tape, state, position)
    #q4 state -----------------------------------------------
    elif(value == '0' and state == 'q4'):
        position = moveL(position)
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q4'):
        replacement = 'b'
        tape = write(tape, position, replacement)
        position = moveL(position)
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q4'):
        replacement = '0'
        tape = write(tape, position, replacement)
        position = moveR(position)
        state = 'q6'
        print tape
        function(tape, state, position)
    #q5 state -----------------------------------------------
    elif(value == '0' and state == 'q5'):
        replacement = 'b'
        tape = write(tape, position, replacement)
        position = moveR(position)
        print tape
        function(tape, state, position)
    elif(value == '1' and state == 'q5'):
        replacement = 'b'
        tape = write(tape, position, replacement)
        position = moveR(position)
        print tape
        function(tape, state, position)
    elif(value == 'b' and state == 'q5'):
        position = moveR(position)
        state = 'q6'
        print tape
        function(tape, state, position)
    #q6 state -----------------------------------------------
    elif(value == '0' and state == 'q6'):
        halt(tape, position, state)
    elif(value == '1' and state == 'q6'):
        halt(tape, position, state)
    elif(value == 'b' and state == 'q6'):
        halt(tape, position, state)

main()
