//package flyweight;

import java.util.HashMap;

public class ShapeFactory {
    public static enum ShapeType {
        LINE, OVAL_FILL, OVAL_NO_FILL;
    }
    
    private static final HashMap<ShapeType, Shape> shapes = new HashMap<ShapeType, Shape>();
    
    public static Shape getShape(ShapeType type) {
        Shape shapeInstance = shapes.get(type);
        
        if (shapeInstance == null) {
            if (type.equals(ShapeType.LINE)) {
                shapeInstance = new Line();
            } else if (type.equals(ShapeType.OVAL_FILL)) {
                shapeInstance = new Oval(true);
            } else if (type.equals(ShapeType.OVAL_NO_FILL)) {
                shapeInstance = new Oval(false);
            } 
            
            shapes.put(type, shapeInstance);
        }
        
        return shapeInstance;
    }
}