public class PigeonMessageService implements MessageService {
    public void sendMessage(String message, String who) {
        System.out.println(String.format("Message send by pigeon to %s with contents: \n%s", who, message));
    }
}