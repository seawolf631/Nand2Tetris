import java.util.*;
import java.lang.*;
import java.io.*;
public class Assembler{
    public static void main(String[] args){
	String fileName = args[0];
	int indexOfDot = fileName.indexOf(".");
	String newFileName = fileName.substring(0,indexOfDot) + ".hack";
	String line = null;
	int counter = 0;
	int variableCounter = 16;
	
	try{
	    // FileReader reads text files in the default encoding.
            FileReader fileReader = new FileReader(fileName);
	    FileWriter fileWriter = new FileWriter(newFileName);
            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = new BufferedReader(fileReader);
	    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
	    
	    //1st Pass through program
	    SymbolTable symbolTable = new SymbolTable();
	    symbolTable.addEntry("SP", 0);
	    symbolTable.addEntry("LCL", 1);
	    symbolTable.addEntry("ARG", 2);
	    symbolTable.addEntry("THIS",3);
	    symbolTable.addEntry("THAT",4);
	    symbolTable.addEntry("SCREEN",16384);
	    symbolTable.addEntry("KBD",24576);
	    symbolTable.addEntry("R0",0);
	    symbolTable.addEntry("R1",1);
	    symbolTable.addEntry("R2",2);
	    symbolTable.addEntry("R3",3);
	    symbolTable.addEntry("R4",4);
	    symbolTable.addEntry("R5",5);
	    symbolTable.addEntry("R6",6);
	    symbolTable.addEntry("R7",7);
	    symbolTable.addEntry("R8",8);
	    symbolTable.addEntry("R9",9);
	    symbolTable.addEntry("R10",10);
	    symbolTable.addEntry("R11",11);
	    symbolTable.addEntry("R12",12);
	    symbolTable.addEntry("R13",13);
	    symbolTable.addEntry("R14",14);
	    symbolTable.addEntry("R15",15);
	    while((line = bufferedReader.readLine()) != null){
		
		int offset = line.indexOf("//");
		if(-1 != offset)
		    line = line.substring(0,offset);
		if(line.length() > 0){
		    String tempCommandType = Parser.commandType(line);
		    if(tempCommandType.equals("L_COMMAND")){
			int endingIndex = line.indexOf(")");
			String label = line.substring(1,endingIndex);
			if(symbolTable.contains(label) == false)
			    symbolTable.addEntry(label, counter);
		    }
		    if(tempCommandType.equals("A_COMMAND"))
			counter++;
		    else if(tempCommandType.equals("C_COMMAND"))
			counter++;
		    System.out.println(line);
		    
		}
	    }
	    bufferedReader.close();

	    
	    //2nd Pass through program
	    // FileReader reads text files in the default encoding.
            fileReader = new FileReader(fileName);
	    fileWriter = new FileWriter(newFileName);
            // Always wrap FileReader in BufferedReader.
            bufferedReader = new BufferedReader(fileReader);
	    bufferedWriter = new BufferedWriter(fileWriter);
	    
	    //bufferedReader = new BufferedReader(fileReader);
	    while((line = bufferedReader.readLine()) != null){
		int offset = line.indexOf("//");
		if(-1 != offset)
		    line = line.substring(0,offset);
		line = line.trim();
		if(line.length() > 0){
		    System.out.println(line);
		    String tempCommandType = Parser.commandType(line);
		    System.out.println(tempCommandType);
		
		    if(tempCommandType.equals("A_COMMAND")){
			String toBinary;
			String binaryNum;
			try{
			    toBinary = Parser.symbol(line);
			    int binaryToInt = Integer.parseInt(toBinary);
			    binaryNum = Integer.toBinaryString(binaryToInt);
			}catch(NumberFormatException e){
			    toBinary = Parser.symbol(line);
			    if(symbolTable.contains(toBinary)){
				binaryNum = Integer.toBinaryString(symbolTable.getAddress(toBinary));
				
			    }
			    else{
				symbolTable.addEntry(toBinary, variableCounter);
				variableCounter++;
				binaryNum = Integer.toBinaryString(symbolTable.getAddress(toBinary));
			    }
			}
			while(binaryNum.length() < 16){
			    binaryNum = "0" + binaryNum;
			}
			System.out.println(binaryNum + "  "+toBinary);
			bufferedWriter.write(binaryNum);
			bufferedWriter.newLine();
		    }
		    else if(tempCommandType.equals("C_COMMAND")){
			String tempDest = Parser.dest(line);
		    	String tempComp = Parser.comp(line);
		    	String tempJump = Parser.jump(line);
			System.out.println("tempDest:"+tempDest+"  tempComp:"+tempComp+"  tempJump:"+tempJump);
			System.out.println("111"+Code.comp(tempComp)+Code.dest(tempDest)+Code.jump(tempJump));
			bufferedWriter.write("111"+Code.comp(tempComp)+Code.dest(tempDest)+Code.jump(tempJump));
			bufferedWriter.newLine();
			counter++;
		    }
	    //else if(tempCommandType.equals("L_COMMAND")){

	    //}
	    }
	    }
	    bufferedReader.close();
	    bufferedWriter.close();
	}
	catch(FileNotFoundException ex){
	    System.out.println("Unable to open file '" + fileName + "'");
	}
	
        catch(IOException ex) {
            System.out.println("Error reading file '"  + fileName + "'");                  
            // Or we could just do this: 
            // ex.printStackTrace();
        }
	
    }
}
