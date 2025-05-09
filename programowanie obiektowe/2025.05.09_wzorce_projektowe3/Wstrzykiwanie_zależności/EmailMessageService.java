public class EmailMessageService implements MessageService {
    public void sendMessage(String message, String who) {
        System.out.println(String.format("Message send by email to %s with contents: \n%s", who, message));
    }
}