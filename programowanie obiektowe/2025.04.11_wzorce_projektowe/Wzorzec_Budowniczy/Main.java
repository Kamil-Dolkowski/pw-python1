// Wzorzec Budowniczy

// foo(int a1=1, int a2=2, int a3=3)

// foo(5,6,7) -> a1=5, a2=6, a3=7
// foo(6,7)   -> a1=6, a2=7, a3=3
// foo(7)     -> a1=7, a2=2, a3=3
// foo()      -> a1=1, a2=2, a3=3

// foo(a1=9, a3=8)

public class Main
{
	public static void main(String[] args) {
		// Vehicle v = new Vehicle.VehicleBuilder("4", "2").hasHorn(false).build();
		Vehicle v = new Vehicle.VehicleBuilder("4", "2").build();
		
		// === Inna koncepcja: ===
		// Vehicle v = new Vehicle.VehicleBuilder("4", "2");
		// v.setHasHeating(true);
		// v.setHasHorn(false);
		
		System.out.println(v.toString());
	}
}