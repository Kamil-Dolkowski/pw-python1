public class Triangle implements Shape {
    public Triangle() {
        System.out.println("-triangle- waiting for draw");
    }
    
    public void draw(String fillColor) {
        System.out.println("Drawing -triangle- with color " + fillColor);
    }
}