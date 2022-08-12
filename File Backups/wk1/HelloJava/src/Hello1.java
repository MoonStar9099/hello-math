
public class Hello1 {

	public void getData() {
		System.out.println("In getData");

		String initStr = "sauerkraut";
		

		char inputChar[] = initStr.toCharArray();
		int len = inputChar.length;
		char outputChar[] = new char[len];
		
		
		
		System.out.println("In getData length " + inputChar.length);

		if (len % 2 == 0) {

			for (int i = 0; i < len / 2; i++) {
				outputChar[i] = inputChar[len-1-i];
				outputChar[len-1-i] = inputChar[i];
				
				System.out.println("outputChar[i] = " + outputChar[i] );
				System.out.println("outputChar[len-1-i]" + outputChar[len-1-i]);
				}
			System.out.println("the reverse string is " +  String.valueOf(outputChar));
			
		} else {
			System.out.println("This si for Odd");

		}
	}

	public static void main(String args[]) {
		System.out.println("hello java");

		Hello1 h2 = new Hello1();
		h2.getData();
	}

}
