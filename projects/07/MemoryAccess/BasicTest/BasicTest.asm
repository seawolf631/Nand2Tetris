//Pushing
@10
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Local
@0

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
@0

D=A
@LCL
A=M
D=A-D
@LCL
M=D
//Pushing
@21
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@22
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Argument
@2

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
@2

D=A
@ARG
A=M
D=A-D
@ARG
M=D
//Popping with Argument
@1

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
@1

D=A
@ARG
A=M
D=A-D
@ARG
M=D
//Pushing
@36
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with This
@6

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
@6

D=A
@THIS
A=M
D=A-D
@THIS
M=D
//Pushing
@42
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@45
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with That
@5

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
@5

D=A
@THAT
A=M
D=A-D
@THAT
M=D
//Popping with That
@2

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
@2

D=A
@THAT
A=M
D=A-D
@THAT
M=D
//Pushing
@510
D=A
@SP
A=M
M=D
@SP
M=M+1
//Popping with Temp
@SP
M=M-1
A=M
D=M
@11
M=D
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
//Pushing with That
@5

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
//Pushing with This
@6

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
//Pushing with This
@6

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
//Pushing with Temp
@11
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
