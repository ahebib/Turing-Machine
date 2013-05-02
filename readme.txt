Universal Turning Machine

Runtime Analysis:

Subtraction:
Input: 5 - 4
Runtime: 1367442528.74 ms = 1.36744e6

Busy Beaver 3:
Input: bbbbbbbbbb
Runtime: 1367442558.48 ms = 1.36744e6

Busy Beaver 4:
Input: bbbbbbbbbb
Runtime: 1367442602.14 ms = 1.36744e6

Beaver 4 took longer than beaver 3.  This is because beaver 4 has more transition steps, and it takes more steps to finish.

Note: The non-terminating example ran into a problem that the max recursion calls was reached so I extended it at the top.
      Eventually python will stop working after it is run.


------------------------------------------------------------------------

		How to set up your own transition table

------------------------------------------------------------------------

Step 1:
	Create a function that will ask the user for an input.  This function should be called from the main to initiate it.
	The calls that are currently there can be commented out by putting a # in front of them or you can add your function to
	the if statement.
		example: variable = raw_input('Please input a combination of 1, 0, and b: ')

Step 2:
	In that function now you have to make that input variable into an array.  You do this by: tape.stringToArray(variable)
	The object tape has a method that takes the string and turns it into an array.

Step 3:
	Call the functions initState() and start()
	initState() will return the q0 state and start will return the initial position of the head which is 0 in the array.

Step 4: Now that you have a state, position, and a tape with some kind of input it's time to create a new function that will contain the
	transitions.  This function will accept the arguments tape, state, and position.

Step 5: In this new function you can write your new transitions with if states like I did or use your own way of coding.  But can still use
	my functions that perform everything a turing machine can which is halt, move left, move right, read, and write.  The proper way to
	call these function with the correct arguments is as follows:

			READ:
			    value = read(tape, position)
			WRITE:
			    replacement = 'new input'
			    tape = write(tape, position, replacement)
			MOVE RIGHT:
			    position, tape = moveR(position, tape)
			MOVE LEFT:
			    position, tape = moveL(position, tape)
			HALT:
			    halt(tape, position, state)

	The way that I approached this program is by using if statements to change the value, position, and state.  The example below
	was was copied from my code:
				
				    value = read(tape, position)
				    if(value == '0' and state == 'q0'):
        				replacement = 'b'
        				tape = write(tape, position, replacement)
        				position, tape = moveR(position, tape)
        				#change state
        				state = 'q1'
        				#recall function with new state
        				function(tape, state, position)
				    elif(value == 'b' and state == 'q0'):
        				halt(tape, position, state)

	In the code above I check the value on tape and if it meets the state and value requirements in the if statement it executes everything in
	the if statement and then recalls the function with the tape, state, and position.  This will go on till a value and a state appear that has
	a halt function call.

	
		