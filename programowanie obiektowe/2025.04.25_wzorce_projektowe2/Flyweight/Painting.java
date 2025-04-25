//package flyweight;

//import flyweight.ShapeFactory.ShapeType;

public class Painting {
    private static ShapeFactory.ShapeType shapes[] = {ShapeFactory.ShapeType.LINE, ShapeFactory.ShapeType.OVAL_FILL, ShapeFactory.ShapeType.OVAL_NO_FILL};
	private static String colors[] = {"red", "blue", "green", "orange", "violet"};
	
	int areaWidth;
	int areaHeight;
	
	public Painting(int width, int height) {
	    areaWidth = width;
	    areaHeight = height;
	}
	
	public void paint() {
	    for (int i=0; i<10; i++) {
	        Shape shape = ShapeFactory.getShape(getRandomShape());
    	    int p[] = getShapeParams();
    	    String color = getRandomColor();
    	    shape.draw(p[0],p[1],p[2],p[3],color);
    	    System.out.println("------------------------------------");
	    }
	}
	
	private ShapeFactory.ShapeType getRandomShape() {
	    int i = (int)(Math.random() * shapes.length);
	    return shapes[i];
	}
	
	private String getRandomColor() {
	    int i = (int)(Math.random() * colors.length);
	    return colors[i];
	}
	
	private int[] getShapeParams() {
	    int x = (int)(Math.random() * areaWidth);
	    int y = (int)(Math.random() * areaHeight);
	    int w = (int)(Math.random() * areaWidth);
	    int h = (int)(Math.random() * areaHeight);
	    
	    int r[] = {x,y,w,h};
	    
	    return r;
	}
}