// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

	@SCREEN
	D = A
	@address
	M = D

	@KBD
	D = A
	@keyboardAddress
	M = D
(WHATSKEY)
	@24576
	D = M
	
	@ISZERO
	D;JEQ
	@LOOP
	D;JGT
(RESTART)
	@SCREEN
	D = A
	@address
	M = D

	@KBD
	D = A
	@keyboardAddress
	M = D
	@WHATSKEY
	0;JMP
(LOOP)
	
	//
	@16
	D=M
	@24576
	D = D - A
	@RESTART
	D;JEQ
	//
	@address
	A = M
	M = -1	

	@1
	D = A
	
	@address
	M = M + D
	
	@WHATSKEY
	0;JMP
(END)
	@END
	0;JMP
(ISZERO)
	//
	@16
	D=M
	@24576
	D = D - A
	@RESTART
	D;JEQ
	//
	@address
	A = M
	M = 0	

	@1
	D = A
	
	@address
	M = M + D
	
	@WHATSKEY
	0;JMP
