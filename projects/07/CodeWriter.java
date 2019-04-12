import java.util.*;
import java.lang.*;
import java.io.*;
public class CodeWriter{
    FileWriter fileWriter;
    static BufferedWriter bufferedWriter;
    public CodeWriter(String fileOutput){
	try{
	    int indexOfDot = fileOutput.indexOf(".");
	    String newFileName = fileOutput.substring(0,indexOfDot) + ".asm";
	    String currentLine = Parser.line;
	    this.fileWriter = new FileWriter(newFileName);
	    this.bufferedWriter = new BufferedWriter(fileWriter);
	    System.out.println("Where am i");
	    if(Parser.commandType.equals("C_PUSH") || Parser.commandType.equals("C_POP")){
		writePushPop(Parser.commandType, Parser.arg1(currentLine), Parser.arg2(currentLine));
	    }
	    
	    //else if(Parser.commandType.equals("C_ARITHMETIC"))
	    //	writeArithmetic(Parser.line);
	}
	catch(FileNotFoundException ex){
	    System.out.println("Unable to open file '" + fileOutput + "'");
	}
	catch(IOException ex){
	    ex.printStackTrace();
	}
    }
    public void setFileName(String fileName){}
    public void writeArithmetic(String command){
	if(command.equals("add")){}
	else if(command.equals("sub")){}
	else if(command.equals("neg")){}
	else if(command.equals("eq")){}
	else if(command.equals("gt")){}
	else if(command.equals("lt")){}
	else if(command.equals("and")){}
	else if(command.equals("or")){}
	else if(command.equals("not")){}
    }
    public static void writePushPop(String commandType, String segment, int index){
	if(commandType.equals("C_PUSH")){
	    System.out.println("FUCCCK");
	    try{
		bufferedWriter.write("@" + index);
		bufferedWriter.newLine();
		bufferedWriter.write("D=A");
		bufferedWriter.newLine();
		bufferedWriter.write("@SP");
		bufferedWriter.newLine();
		bufferedWriter.write("M=D");
	    }
	    catch(IOException ex){
		ex.printStackTrace();
	    }
	    }
	else if(commandType.equals("C_POP")){
	    //bufferedWriter.write();
	    //bufferedWriter.newLine();
	    }
    }
    public void close(){
	try{
	    bufferedWriter.close();
	}
	catch(IOException ex){
	    ex.printStackTrace();
	}
    }
    public static void main(String[] args){}
}
