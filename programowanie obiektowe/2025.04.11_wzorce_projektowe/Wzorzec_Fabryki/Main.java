// Wzorzec Fabryki

public class Main
{
	public static void main(String[] args) {
		Car c = (Car)Factory.getVehicle("car", 4, 4);
		Bicycle b = (Bicycle)Factory.getVehicle("bicycle", 2, 1);
		
		// Car c = new Car(4, "4");
		// Bicycle b = new Bicycle("2", 1);
		
		System.out.println(c.toString());
		System.out.println(b.toString());
	}
}