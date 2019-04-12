//Bootstrap
//@256
//D=A
//@SP
//M=D
//Writing Function
(Sys.init)
//Writing Call
//push return-address
@RETURNADDRESS131000
D=A
@SP
A=M
M=D
//push LCL
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
//push ARG
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
//push THIS
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
//push THAT
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
//ARG = SP-n-5
@SP
M=M+1
D=M
@0

D=D-A
@5
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto f
@Sys.main
0;JMP
//(return-address)
(RETURNADDRESS131000)
//Popping with Temp
@SP
M=M-1
A=M
D=M
@6
M=D
//Labeling
(LOOP)
//Writing GOTO
@LOOP
0;JMP
//Writing Function
(Sys.main)
//Pushing
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
//Writing Call
//push return-address
@RETURNADDRESS272000
D=A
@SP
A=M
M=D
//push LCL
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
//push ARG
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
//push THIS
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
//push THAT
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
//ARG = SP-n-5
@SP
M=M+1
D=M
@1

D=D-A
@5
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto f
@Sys.add12
0;JMP
//(return-address)
(RETURNADDRESS272000)
//Popping with Temp
@SP
M=M-1
A=M
D=M
@5
M=D
//Pushing
@246
D=A
@SP
A=M
M=D
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
//Writing Function
(Sys.add12)
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
@SP
A=M
M=0
@SP
M=M+1
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
@12
D=A
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
//Writing Return
//Frame = LCL
@LCL
D=M
@frame
M=D
//RET = *(FRAME-5)
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
