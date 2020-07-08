// Take three numbers from the user and print the greatest number.

import java.util.*;

public class GreatestNumber {
	
	public static void main(String[] args) {
		int x, y, z;
		Scanner keyboard = new Scanner(System.in);
		System.out.println("Enter your first number ");
		x = keyboard.nextInt();
		
		System.out.println("Enter your second number ");
		y = keyboard.nextInt();
		
		System.out.println("Enter your third number ");
		z = keyboard.nextInt();
		
		if (x > y) {
			
			if (x > z) {System.out.println(+ x + " (x) is the largest number");}
			
		}
		else if (y > x) {
			
			if (y > z)
			System.out.println(+ y + " (y) is the largest number");
			
		}
		
		else  {
			System.out.println(+ z + " (z)is the largest number");
		}

	}

}
