import java.util.List;
import java.util.ArrayList;

public class CompoundShape implements Shape {
    private List<Shape> elements = new ArrayList<Shape>();
    
    public void addShape(Shape s) {
        this.elements.add(s);
    }
    
    public void draw(String fillColor) {
        for (Shape s: elements) {
            s.draw(fillColor);
        }
    }
}