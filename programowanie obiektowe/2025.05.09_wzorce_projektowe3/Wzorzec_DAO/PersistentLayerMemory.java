import java.util.ArrayList;

public class PersistentLayerMemory implements CarDAO {
    // This is our "database"
    private ArrayList<Car> cars;
    
    public PersistentLayerMemory() {
        cars = new ArrayList<Car>();
        
        cars.add(new Car("Aston Martin", "DB12", 5939));
        cars.add(new Car("Aston Martin", "DBX", 5939));
        cars.add(new Car("FIAT", "126p", 600));
        cars.add(new Car("Mercedes", "S", 2989));
        cars.add(new Car("Mercedes", "S", 2999));
    }
    
    public ArrayList<Car> getAllCars() {
        return cars;
    }
    
    public ArrayList<Car> getCarByMarkaModel(String marka, String model) {
        ArrayList<Car> selected = new ArrayList<Car>();
        
        for (Car car: cars) {
            boolean cond1 = car.getMarka().equals(marka);
            boolean cond2 = car.getModel().equals(model);
            
            if (cond1 && cond2) {
                selected.add(car);
            }
        }
        
        return selected;
    }
    
    public void addCar(Car car) {
        cars.add(car);
    }
}