public class Rectangle implements Shape {
    public Rectangle() {
        System.out.println("-rectangle- waiting for draw");
    }
    
    public void draw(String fillColor) {
        System.out.println("Drawing -rectangle- with color " + fillColor);
    }
}