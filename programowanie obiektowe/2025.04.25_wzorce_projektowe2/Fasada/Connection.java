public class Connection {
    private String type = "";
    
    public Connection(String type) {
        this.type = type;
        System.out.println("Create connection for " + type);
    }
}