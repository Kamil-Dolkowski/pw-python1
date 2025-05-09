public class EmailMessageServiceInjector implements MessageServiceInjector {
    public Messanger getMessanger() {
        return new MessangerImplementation(new EmailMessageService());
    }
}