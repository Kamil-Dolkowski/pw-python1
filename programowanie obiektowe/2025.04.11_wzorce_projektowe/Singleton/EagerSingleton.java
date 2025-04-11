// Singleton
// - prywatny konstruktor
// - zmienna prywatna przechowująca instancję klasy
// - publiczna metoda statyczna zwracająca instancję lub wywołująca konstruktor

// EagerSingleton - Singleton "Zachłanny"

class EagerSingleton {
    private static final EagerSingleton instance = new EagerSingleton();
    private int x=456;
    
    private EagerSingleton() {
        System.out.println("Construct ...");
    }
    
    public static EagerSingleton getInstance() {
        return instance;
    }
    
    public void setX(int x) {
        this.x = x;
    }
    
    public int getX() {
        return x;
    }
}

public class Main
{
	public static void main(String[] args) {
		EagerSingleton s1 = EagerSingleton.getInstance();
		EagerSingleton s2 = EagerSingleton.getInstance();
		
		s1.setX(123);
		System.out.println(s2.getX());
	}
}