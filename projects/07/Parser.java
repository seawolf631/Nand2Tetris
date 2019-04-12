import java.util.*;
import java.lang.*;
import java.io.*;
public class Parser{
    static String commandType;
    static String line;
    static boolean fileOpen = false;
    static String[] arithmeticCommands = {"add","sub", "neg", "eq", "gt","lt","and","or","not"};
    public Parser(String fileName){
	try{
	    FileReader fileReader = new FileReader(fileName);
	    BufferedReader bufferedReader = new BufferedReader(fileReader);
	    line = null;
	    while((line = bufferedReader.readLine()) != null){
		fileOpen = true;
		//Getting Rid of Comments and White Space
		int offset = line.indexOf("//");
		if(-1 != offset)
		    line = line.substring(0,offset);
		line = line.trim();
		if(line.length() > 0){
		    System.out.println(line);
		    commandType = commandType(line);
		    System.out.print("Command: "+ commandType + "  arg1: "+ arg1(line));
		    if(commandType.equals("C_PUSH") || commandType.equals("C_POP") || commandType.equals("C_FUNCTION") || commandType.equals("C_CALL"))
			System.out.print("  arg2: " + arg2(line));
		    System.out.println();
		}
	    }
	    bufferedReader.close();
	}
	catch(FileNotFoundException ex){
	    System.out.println("Unable to open file '" + fileName + "'");
	}
	catch(IOException ex){
	    ex.printStackTrace();
	}
    }
    public static boolean hasMoreCommands(){
	return fileOpen;
    }
    //public void advance(){}
    public static String commandType(String currentLine){
	//Eliminating everything besides first word
	int space = currentLine.indexOf(" ");
	String firstWord;
	if(-1 != space)
	    firstWord = currentLine.substring(0, space);
	else
	    firstWord = currentLine;
	//Checking first command
	if(firstWord.equals("push"))
	   return "C_PUSH";
	else if(firstWord.equals("pop"))
	    return "C_POP";
	else if(Arrays.asList(arithmeticCommands).contains(firstWord))
	    return "C_ARITHMETIC";
	else
	    return null;
    }
    public static String arg1(String currentLine){
	String commandType = commandType(currentLine);
	if(!(commandType.equals("C_ARITHMETIC"))){
	    int firstSpace = currentLine.indexOf(" ");
	    int secondSpace = currentLine.indexOf(" ", firstSpace+1);
	    return currentLine.substring(firstSpace+1, secondSpace);
	}
	else
	    return currentLine;
    }
    public static int arg2(String currentLine){
	String commandType = commandType(currentLine);
	int firstSpace = currentLine.indexOf(" ");
	int secondSpace = currentLine.indexOf(" ", firstSpace+1);
	String arg2 = currentLine.substring(secondSpace+1, currentLine.length());
	return Integer.parseInt(arg2);
    }
    public static void main(String[] args){}
}
