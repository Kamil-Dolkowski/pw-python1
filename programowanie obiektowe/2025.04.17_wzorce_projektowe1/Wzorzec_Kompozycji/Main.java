public class Main
{
	public static void main(String[] args) {
		Drawing d = new Drawing();
		
		d.addShape(new Triangle());
		d.addShape(new Rectangle());
		
		CompoundShape cs = new CompoundShape();
		cs.addShape(new Rectangle());
		cs.addShape(new Rectangle());
		cs.addShape(new Circle());
		
		d.addShape(cs);
		
		d.draw(1, "yellow");
		d.draw(3, "red");
	}
}