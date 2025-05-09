import java.util.ArrayList;

public interface CarDAO {
    ArrayList<Car> getAllCars();
    ArrayList<Car> getCarByMarkaModel(String marka, String model);
    void addCar(Car car);
}