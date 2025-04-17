public class SocketAdapterComposition implements SocketAdapterDC {
    private Socket socket = new Socket();
    
    public Power get5DC() {
        Power p = socket.getPower(); // zwraca 230
        return convertPower(p, Power.Type.DC, 46);
    }
    
    public Power get12DC() {
        Power p = socket.getPower();
        return convertPower(p, Power.Type.DC, 19);
    }
    
    public Power get24DC() {
        Power p = socket.getPower();
        return convertPower(p, Power.Type.DC, 9);
    }
        
    private Power convertPower(Power power, Power.Type type, int conversion) {
        int volts = power.getVoltage();
        int newVolts = volts / conversion;
        return new Power(type, newVolts);
    }
}