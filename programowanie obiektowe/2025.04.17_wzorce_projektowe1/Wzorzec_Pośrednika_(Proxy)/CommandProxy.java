public class CommandProxy implements CommandExecutor {
    private CommandExecutor executor;
    private boolean isPriviledges;
    
    public CommandProxy(String login, String password) {
        if (login.equals("aston") && password.equals("martin")) {
            isPriviledges = true;
        } else {
            isPriviledges = false;
        }
        
        executor = new CommandExecutorImplementation();
    }
    
    public void execute(String cmd) {
        if (cmd.equals("Launch rockets") && !isPriviledges) {
            System.out.println("You are not authorized to do this destructive action");
        }
        else if (cmd.equals("Breaking law") && !isPriviledges) {
            System.out.println("You must be Aston Martin to break law");
        } else {
            executor.execute(cmd);
        }
    }
}