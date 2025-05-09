public class Main
{
	public static void main(String[] args) {
		String message = "Hello World!";
		String email = "who@where.org";
		String coordinates = "HM6H+7G";
		
		MessageServiceInjector injector = null;
		Messanger messanger = null;
		
		injector = new PigeonMessageServiceInjector();
		messanger = injector.getMessanger();
		messanger.processMessage(message, coordinates);
		
		injector = new EmailMessageServiceInjector();
		messanger = injector.getMessanger();
		messanger.processMessage(message, email);
	}
}