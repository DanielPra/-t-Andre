// The first value is for today’s day of the week and must be from 0 to 6, for
//  today’s day of the week. The program should display an appropriate error
//  message if the entered value is not from 0 to 6

// The second value is to compute the future day. The future day is computed by adding the
// second value to the first value.

// The program should then determine and print today’s day of the week and the
// future day of the week based on codes as follows: Sunday is 0, Monday is 1,
// …, and Saturday is 6


import java.util.Scanner;
public class Days {

	public static void main(String[] args) {
    int NumToday, NumFuture, CalcFuture;
    Scanner scanner = new Scanner(System.in);
		System.out.println("Enter number 0-6 for today's day");
    NumToday = scanner.nextInt();
    System.out.println("Enter number 0-6 for the future day");
    NumFuture = scanner.nextInt();

    CalcFuture = NumToday + NumFuture;
    System.out.println("\nThe future day is " + CalcFuture);


    //TODO: Fix exception handling for above

/*

    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    */


	}

}
