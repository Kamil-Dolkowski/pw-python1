public class Vehicle {
    // Must-have (required) parameters
    private String wheels;
    private String seats;
    
    // Optional parameters
    private boolean hasHeatingSeats;
    private boolean hasHorn;
    
    public String getNumberOfWheels() {
        return wheels;
    }
    public String getNumberOfSeats() {
        return seats;
    }
    
    public boolean hasHeatingSeats() {
        return hasHeatingSeats;
    }
    public boolean hasHorn() {
        return hasHorn;
    }
    
    public String toString() {
        String w = getNumberOfWheels();
        String s = getNumberOfSeats();
        String st = "This wehicle has " + w + " wheels and " + s + " seats.";
        
        if (hasHeatingSeats) {
            st += " It has heating seats.";
        }
        if (hasHorn) {
            st += " It has horn.";
        }
        
        return st;
    }
    
    private Vehicle(VehicleBuilder builder) {
        this.wheels = builder.wheels;
        this.seats = builder.seats;
        this.hasHeatingSeats = builder.hasHeatingSeats;
        this.hasHorn = builder.hasHorn;
    }
    
    public static class VehicleBuilder {
        // Must-have (required) parameters
        private String wheels;
        private String seats;
        
        // Optional parameters
        private boolean hasHeatingSeats;
        private boolean hasHorn;
        
        public VehicleBuilder(String wheels, String seats) {
            this.wheels = wheels;
            this.seats = seats;
            this.hasHeatingSeats = false;
            this.hasHorn = true;
        }
        
        public VehicleBuilder hasHeatingForSeats(boolean has) {
            hasHeatingSeats = has;
            return this;
        }
        
        public VehicleBuilder hasHorn(boolean has) {
            hasHorn = has;
            return this;
        }
        
        public Vehicle build() {
            return new Vehicle(this);
        }
    }
}