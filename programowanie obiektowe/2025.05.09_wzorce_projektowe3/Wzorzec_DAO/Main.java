public class Main
{
	public static void main(String[] args) {
		CarDAO dao = new PersistentLayerMemory();
		
		for (Car car: dao.getCarByMarkaModel("Mercedes", "S")) {
		    System.out.println(car.getPojemnosc());
		}
		
		dao.addCar(new Car("Ferrari", "Testarossa", 4941));
		
		for (Car car: dao.getAllCars()) {
		    String marka = car.getMarka();
		    String model = car.getModel();
		    String pojemnosc = car.getPojemnosc();
		    
		  //  System.out.println(marka + " " + model + " " + pojemnosc);
		    System.out.println(String.format("%s %s %s", marka, model, pojemnosc));
		}
	}
}