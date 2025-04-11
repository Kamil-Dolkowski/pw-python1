public class Bicycle extends Vehicle {
    private String wheels;
    private int seats;
    
    public Bicycle(String wheels, int seats) {
        this.wheels = wheels;
        this.seats = seats;
    }
    
    public String getNumberOfWheels() {
        return wheels;
    }
    
    public String getNumberOfSeats() {
        return Integer.toString(seats);
    }
}