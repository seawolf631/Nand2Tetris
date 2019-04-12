import java.util.*;
public class SymbolTable{
    Hashtable symbolTable;
    public SymbolTable(){
	this.symbolTable = new Hashtable();
    }
    public void addEntry(String symbol, int address){
	symbolTable.put(symbol, address);
    }
    public boolean contains(String symbol){
	return symbolTable.containsKey(symbol);
    }
    public int getAddress(String symbol){
	int address = Integer.valueOf((symbolTable.get(symbol)).toString());
	if(address >= 0)
	    return address;
	else
	    return -1;
    }
    public static void main(String[] args){
	SymbolTable symbolTable = new SymbolTable();
	symbolTable.addEntry("SP",0);
	symbolTable.addEntry("LCL", 1);
	symbolTable.addEntry("ARG", 2);
	symbolTable.addEntry("THIS",3);
	symbolTable.addEntry("THAT",4);
	symbolTable.addEntry("SCREEN",16384);
	symbolTable.addEntry("KBD",24576);
	System.out.println(symbolTable.getAddress("SP"));
	System.out.println(symbolTable.getAddress("LCL"));
	System.out.println(symbolTable.getAddress("ARG"));
	System.out.println(symbolTable.getAddress("THIS"));
	System.out.println(symbolTable.getAddress("THAT"));
	System.out.println(symbolTable.getAddress("SCREEN"));
	System.out.println(symbolTable.getAddress("KBD"));
    }
}
