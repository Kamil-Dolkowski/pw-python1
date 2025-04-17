public class Main
{
	public static void main(String[] args) {
		test();
	}
	
	private static void test() {
	   // SocketAdapterDC adapter = new SocketAdapterInheritance();
	    
	    SocketAdapterDC adapter = new SocketAdapterComposition();
	
	    Power v5DC = getPower(adapter, Power.Type.DC, 5);
	    Power v12DC = getPower(adapter, Power.Type.DC, 12);
	    Power v30DC = getPower(adapter, Power.Type.DC, 30);
	    
	    if (v5DC != null) {
	        System.out.println(v5DC.toString());
	    } else {
	        System.out.println("Problems with power adapter");
	    }
	    if (v12DC != null) {
	        System.out.println(v12DC.toString());
	    } else {
	        System.out.println("Problems with power adapter");
	    }
	    if (v30DC != null) {
	        System.out.println(v30DC.toString());
	    } else {
	        System.out.println("Problems with power adapter");
	    }
	    
	}
	
	private static Power getPower(SocketAdapterDC adapter, Power.Type type, int voltage) {
	    if (type == Power.Type.DC) {
	        switch (voltage) {
	            case 5: return adapter.get5DC();
	            case 12: return adapter.get12DC();
	            case 24: return adapter.get24DC();
	            default: return null;
	        }
	    }
	    return null;
	}
}