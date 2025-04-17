public class SocketAdapterInheritance extends Socket implements SocketAdapterDC {
    public Power get5DC() {
        Power p = getPower(); // zwraca 230
        return convertPower(p, Power.Type.DC, 46);
    }
    
    public Power get12DC() {
        Power p = getPower();
        return convertPower(p, Power.Type.DC, 19);
    }
    
    public Power get24DC() {
        Power p = getPower();
        return convertPower(p, Power.Type.DC, 9);
    }
        
    private Power convertPower(Power power, Power.Type type, int conversion) {
        int volts = power.getVoltage();
        int newVolts = volts / conversion;
        return new Power(type, newVolts);
    }
}