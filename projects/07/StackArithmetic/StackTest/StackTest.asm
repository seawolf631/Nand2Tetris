//Pushing
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//Equals
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@EQUAL70100
D;JEQ
@SP
A=M
M=0
@EQUAL70101
0;JMP
(EQUAL70100)
@SP
A=M
M=-1
(EQUAL70101)
@SP
M=M+1
//Pushing
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//Equals
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@EQUAL13100
D;JEQ
@SP
A=M
M=0
@EQUAL13101
0;JMP
(EQUAL13100)
@SP
A=M
M=-1
(EQUAL13101)
@SP
M=M+1
//Pushing
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//Equals
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@EQUAL20100
D;JEQ
@SP
A=M
M=0
@EQUAL20101
0;JMP
(EQUAL20100)
@SP
A=M
M=-1
(EQUAL20101)
@SP
M=M+1
//Pushing
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//Less-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@LESSTHAN31100
D;JLT
@SP
A=M
M=0
@LESSTHAN31101
0;JMP
(LESSTHAN31100)
@SP
A=M
M=-1
(LESSTHAN31101)
@SP
M=M+1
//Pushing
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//Less-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@LESSTHAN45100
D;JLT
@SP
A=M
M=0
@LESSTHAN45101
0;JMP
(LESSTHAN45100)
@SP
A=M
M=-1
(LESSTHAN45101)
@SP
M=M+1
//Pushing
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//Less-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@LESSTHAN19100
D;JLT
@SP
A=M
M=0
@LESSTHAN19101
0;JMP
(LESSTHAN19100)
@SP
A=M
M=-1
(LESSTHAN19101)
@SP
M=M+1
//Pushing
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//Greather-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@GREATERTHAN1100
D;JGT
@SP
A=M
M=0
@GREATERTHAN1101
0;JMP
(GREATERTHAN1100)
@SP
A=M
M=-1
(GREATERTHAN1101)
@SP
M=M+1
//Pushing
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//Greather-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@GREATERTHAN64100
D;JGT
@SP
A=M
M=0
@GREATERTHAN64101
0;JMP
(GREATERTHAN64100)
@SP
A=M
M=-1
(GREATERTHAN64101)
@SP
M=M+1
//Pushing
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//Greather-Than
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
A=M
D=A-D
@GREATERTHAN85100
D;JGT
@SP
A=M
M=0
@GREATERTHAN85101
0;JMP
(GREATERTHAN85100)
@SP
A=M
M=-1
(GREATERTHAN85101)
@SP
M=M+1
//Pushing
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//Pushing
@53
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
//Pushing
@112
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
//Negate
@SP
M=M-1
A=M
M=-M
@SP
M=M+1
//AND
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D&M
@SP
M=M-1
M=M-1
A=M
M=D
@SP
M=M+1
//Pushing
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//OR
@SP
A=M
A=A-1
A=A-1
D=M
A=A+1
D=D|M
@SP
M=M-1
M=M-1
A=M
M=D
@SP
M=M+1
//NOT
@SP
A=M
A=A-1
D=M
D=!D
M=D