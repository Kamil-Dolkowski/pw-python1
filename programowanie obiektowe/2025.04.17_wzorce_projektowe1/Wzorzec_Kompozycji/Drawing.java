import java.util.List;
import java.util.ArrayList;

public class Drawing {
    private List<Shape> shapes = new ArrayList<Shape>();
    
    public void addShape(Shape s) {
        this.shapes.add(s);
    }
    
    public void draw(int what, String fillColor) {
        if (what >= 1 && what <= shapes.size()) {
            shapes.get(what-1).draw(fillColor);
        }
        
    }
}