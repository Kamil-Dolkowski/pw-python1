// Singleton
// - prywatny konstruktor
// - zmienna prywatna przechowująca instancję klasy
// - publiczna metoda statyczna zwracająca instancję lub wywołująca konstruktor

// LazySingleton - Singleton "Leniwy"

class LazySingleton {
    private static LazySingleton instance;
    private int x=456;
    
    private LazySingleton() {
        System.out.println("Construct ...");
    }
    
    public static LazySingleton getInstance() {
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
		LazySingleton s1 = LazySingleton.getInstance();
		LazySingleton s2 = LazySingleton.getInstance();
		
		s1.setX(123);
		System.out.println(s2.getX());
	}
}