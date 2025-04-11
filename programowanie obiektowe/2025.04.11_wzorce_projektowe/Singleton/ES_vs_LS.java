// Singleton
// - prywatny konstruktor
// - zmienna prywatna przechowująca instancję klasy
// - publiczna metoda statyczna zwracająca instancję lub wywołująca konstruktor

class EagerSingleton {
    public static final EagerSingleton instance = new EagerSingleton();
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

class LazySingleton {
    public static LazySingleton instance;
    private int x=456;
    
    private LazySingleton() {
        System.out.println("Construct ...");
    }
    
    // synchronized - chroni przed utworzeniem kilku instancji klasy w przypadku pracy kilku wątków
    public static synchronized LazySingleton getInstance() {
        if (instance == null) {
            instance = new LazySingleton();
        }
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
		// LazySingleton l = LazySingleton.instance;
		// l.setX(123);
		
		EagerSingleton l = EagerSingleton.instance;
		l.setX(123);
		
		System.out.println(l.getX());
	}
}