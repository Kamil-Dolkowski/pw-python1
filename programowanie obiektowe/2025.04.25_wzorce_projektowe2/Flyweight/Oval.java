//package flyweight;

public class Oval implements Shape {
    private boolean fill;
    
    public Oval(boolean f) {
        this.fill = f;
        System.out.println("O: Create oval object with fill set to: " + f);
    }
    
    public void draw(int x, int y, int width, int height, String color) {
        System.out.println("O: Set color for oval object: " + color);
        
        if (fill) {
            System.out.println("OF: Draw oval object: x=" + U.s(x) + ", y=" + U.s(y) + " with filling");
        } else {
            System.out.println("ONF: Draw oval object: x=" + U.s(x) + ", y=" + U.s(y) + " without filling");
        }
    }
}