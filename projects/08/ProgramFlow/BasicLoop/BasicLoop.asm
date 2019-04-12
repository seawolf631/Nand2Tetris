//Pushing
@0    
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Local
@0         // initializes sum = 0

D=A
@LCL
A=M
D=D+A
@LCL
M=D
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
@0         // initializes sum = 0

D=A
@LCL
A=M
D=A-D
@LCL
M=D
//Labeling
(LOOP_START)
//Pushing with Argument
@0    

D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Pushing with Local
@0

D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Adding
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
//Popping with Local
@0	        // sum = sum + counter

D=A
@LCL
A=M
D=D+A
@LCL
M=D
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
@0	        // sum = sum + counter

D=A
@LCL
A=M
D=A-D
@LCL
M=D
//Pushing with Argument
@0

D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//Subtracting
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
//Popping with Argument
@0      // counter--

D=A
@ARG
A=M
D=D+A
@ARG
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@0      // counter--

D=A
@ARG
A=M
D=A-D
@ARG
M=D
//Pushing with Argument
@0

D=A
@ARG
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
//Writing IF-GOTO
@SP
M=M-1
A=M
D=M
@LOOP_START  // If counter > 0, goto LOOP_START
D;JNE
//Pushing with Local
@0

D=A
@LCL
A=M
D=D+A
A=D
D=M
@SP
A=M
M=D
@SP
M=M+1
