public class Power {
    enum Type {
        AC,
        DC
    }
    
    private int volts;
    private Type type; 

    public Power(Type type, int volts) {
        this.type = type;
        this.volts = volts;
    }
    
    public int getVoltage() {
        return volts;
    }
    
    public Type getType() {
        return type;
    }
    
    public String toString() {
        String type = "DC";
        if (type.equals(Type.AC)) {
            type = "AC";
        }
        return "voltage = " + Integer.toString(volts) + ", type = " + type;
    }
}