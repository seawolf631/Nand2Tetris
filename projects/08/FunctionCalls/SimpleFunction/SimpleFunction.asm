//Writing Function
(SimpleFunction.test)
@SP
A=M
M=0
@SP
M=M+1
@SP
A=M
M=0
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
//Pushing with Local
@1

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
//NOT
@SP
A=M
A=A-1
D=M
D=!D
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
//Pushing with Argument
@1

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
//Writing Return
//Frame = LCL
@LCL
D=M
@frame
M=D
//RET = *(FRAME-5)
@frame
D=M
@5
D=D-A
A=D
D=M
@ret
M=D
//*ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//SP = ARG + 1
@ARG
D=M+1
@SP
M=D
//THAT = *(FRAME-1)
@frame
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
//THIS = *(FRAME-2)
@frame
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
//ARG = *(FRAME-3)
@frame
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
//LCL = *(FRAME-4)
@frame
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
//goto RET
@ret
A=M
0;JMP
