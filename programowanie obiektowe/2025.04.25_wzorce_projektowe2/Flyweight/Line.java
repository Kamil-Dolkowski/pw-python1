//package flyweight;

public class Line implements Shape {
    public Line() {
        System.out.println("L: Create line object");
    }
    
    public void draw(int x, int y, int width, int height, String color) {
        System.out.println("L: Set color for line object: " + color);
        System.out.println("L: Draw line object: x=" + U.s(x) + ", y=" + U.s(y));
    }
}