public class Factory {
    public static Vehicle getVehicle(String type, int wheels, int seats) {
        
        if (type.equals("car")) {
            
            return new Car(wheels, Integer.toString(seats));
            
        } else if (type.equals("bicycle")) {
            
            return new Bicycle(Integer.toString(wheels), seats);
            
        }
        
        return null;
    }
}