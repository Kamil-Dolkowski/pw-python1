public class Car extends Vehicle {
    private int wheels;
    private String seats;
    
    public Car(int wheels, String seats) {
        this.wheels = wheels;
        this.seats = seats;
    }
    
    public String getNumberOfWheels() {
        return Integer.toString(wheels);
    }
    
    public String getNumberOfSeats() {
        return seats;
    }
}