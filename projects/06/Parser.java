import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
public class Parser{
    private String fileName;
    static String currentCommand;
    static ArrayList<String> fileLines = new ArrayList<String>();
    public Parser(String fileName){
	
        
    }
    //public static boolean hasMoreCommands(){}
    public void advance(){
	
    }
    public static String commandType(String line){
	    if(line.charAt(0) == '@')
		return "A_COMMAND";
	    else if(line.charAt(0) == '(')
		return "L_COMMAND";
	    else
		return "C_COMMAND";
      
    }
    public static String symbol(String line){
	int stringLength = line.length();
	return line.substring(1,stringLength);
    }
    public static String dest(String line){
	int offset = line.indexOf("=");
	int semiIndex = line.indexOf(";");
	if(-1 != offset)
	    line = line.substring(0,offset);
	else
	    line = "0";
	return line;
    }
    public static String comp(String line){
	String temp = null;
	int equalIndex = line.indexOf("=");
	int semiIndex = line.indexOf(";");
	if(-1 != semiIndex){
	    if(-1 != equalIndex)
		temp = line.substring(equalIndex+1, semiIndex);
	    else
		temp = line.substring(0,semiIndex);
	}
	else
	    if(-1 != equalIndex)
		temp = line.substring(equalIndex + 1, line.length());
	    else
		temp = line;
	return temp;
    }
    public static String jump(String line){
	int offset = line.indexOf(";");
	String temp = null;
	if(-1 != offset)
	    temp = line.substring(offset + 1, line.length());
	return temp;
    }
    public static void main(String[] args){}
}
