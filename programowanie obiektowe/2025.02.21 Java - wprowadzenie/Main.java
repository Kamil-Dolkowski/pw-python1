public class Main
{
	public static void main(String[] args) {
		boolean b = 2 > 1;
		
		if (b) {
		    System.out.println("TTT");
		}
		
		/*
		byte - 8 bitów
		char - 16 bitów
		short - 16 bitów
		int - 32 bity
		long - 64 bity
		*/
		
		byte b1 = 64;
		
		System.out.println(b1);
		
		// b1 = 128;  // error
		b1 = -128;
		
		System.out.println(b1);
		
		char c = 'a';
		
		System.out.println(c);
		
		c = '\u0104';
		
		System.out.println(c);
		
		/*
		float - 32b
		double - 64b
		*/
		
		float f = 1.2f;
		Float ff = 3.4f;
		// Float ff = new Float(f);
		Float ff2 = 1.1f;
		
		System.out.println(f);
		System.out.println(Float.MAX_VALUE);
		System.out.println(ff.toString());
		System.out.println(ff+ff2);
		
		System.out.println((int)Character.MAX_VALUE);
		
		long l = 123_456_789_1011L;
		
		System.out.println(l);
		System.out.println(Long.MAX_VALUE);
	}
}
