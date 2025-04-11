public abstract class Vehicle {
    public abstract String getNumberOfWheels();
    public abstract String getNumberOfSeats();
    
    public String toString() {
        String w = getNumberOfWheels();
        String s = getNumberOfSeats();
        return "This wehicle has " + w + " wheels and " + s + " seats.";
    }
}