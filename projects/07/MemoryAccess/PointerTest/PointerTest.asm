//Pushing
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Pointer
@SP
M=M-1
A=M
D=M
@3
M=D
//Pushing
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Pointer
@SP
M=M-1
A=M
D=M
@4
M=D
//Pushing
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with This
@2

D=A
@THIS
A=M
D=D+A
@THIS
M=D
@SP
M=M-1
A=M
D=M
@THIS
A=M
M=D
@2

D=A
@THIS
A=M
D=A-D
@THIS
M=D
//Pushing
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with That
@6

D=A
@THAT
A=M
D=D+A
@THAT
M=D
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
@6

D=A
@THAT
A=M
D=A-D
@THAT
M=D
//Pushing with Pointer
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
//Pushing with Pointer
@4
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
//Pushing with This
@2

D=A
@THIS
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
//Pushing with That
@6

D=A
@THAT
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
