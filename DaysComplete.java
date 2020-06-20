import java.util.Scanner;
import java.util.InputMismatchException;
public class DaysComplete {

    public static void main(String[] args) {
        int numToday, numFuture, CalcFuture;
        String[] days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday"};
        Scanner scanner = new Scanner(System.in);

        /*System.out.println("Enter number 0-6 for today's day");
        numToday = scanner.nextInt();
        System.out.println("Enter number 0-6 for the future day");
        numFuture = scanner.nextInt();*/


        numToday = ask(scanner, "\nEnter number 0-6 for today's day");
        numFuture = ask(scanner, "\nEnter number 0-6 for the future day");

        CalcFuture = (numToday + numFuture) % 7;
        System.out.println("\nThe future day is " + days[CalcFuture]);


    }

    public static int ask(Scanner scanner, String query) {
        while (true) {
			try	{
				System.out.println(query);
		        return scanner.nextInt();
    	    }
		    catch(InputMismatchException e)	{
				scanner.nextLine();
				System.out.println("You may only enter a digit 0-6 ");
				System.out.println("Please try again");
		    }
	    }
    }
}
