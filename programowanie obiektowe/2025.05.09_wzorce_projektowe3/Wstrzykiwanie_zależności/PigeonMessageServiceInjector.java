public class PigeonMessageServiceInjector implements MessageServiceInjector {
    public Messanger getMessanger() {
        return new MessangerImplementation(new PigeonMessageService());
    }
}