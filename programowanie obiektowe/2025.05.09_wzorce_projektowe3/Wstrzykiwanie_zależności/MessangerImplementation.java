public class MessangerImplementation implements Messanger {
    private MessageService messageService;
    
    public MessangerImplementation(MessageService messageService) {
        this.messageService = messageService;
    }
    
    public void processMessage(String message, String who) {
        messageService.sendMessage(message, who);
    }
}