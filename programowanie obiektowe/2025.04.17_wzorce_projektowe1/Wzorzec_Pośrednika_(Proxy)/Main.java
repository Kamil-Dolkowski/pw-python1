public class Main
{
	public static void main(String[] args) {
		CommandExecutor cepriv = new CommandProxy("aston", "martin");
		
		cepriv.execute("Launch rockets");
		cepriv.execute("Eat dinner");
		
		CommandExecutor ceunpriv = new CommandProxy("fulman", "p");
// 		CommandExecutor ceunpriv = new CommandExecutorImplementation();
		
		ceunpriv.execute("Launch rockets");
		ceunpriv.execute("Eat dinner");
	}
}