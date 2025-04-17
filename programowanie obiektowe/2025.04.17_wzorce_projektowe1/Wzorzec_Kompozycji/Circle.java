public class Circle implements Shape {
    public Circle() {
        System.out.println("-circle- waiting for draw");
    }
    
    public void draw(String fillColor) {
        System.out.println("Drawing -circle- with color " + fillColor);
    }
}