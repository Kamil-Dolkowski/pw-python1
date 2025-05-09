public class Car {
    private String marka;
    private String model;
    private int pojemnosc;
    
    public Car(String marka, String model, int pojemnosc) {
        this.marka = marka;
        this.model = model;
        this.pojemnosc = pojemnosc;
    }
    
    public String getMarka() {
        return marka;
    }
    
    public String getModel() {
        return model;
    }
    
    public String getPojemnosc() {
        return String.valueOf(pojemnosc);
    }
}