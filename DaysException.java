import java.util.Scanner;
import java.util.InputMismatchException;
public class DaysException {

	public static void main(String[] args) {


    int NumToday, NumFuture;
    Scanner scanner = new Scanner(System.in);
		boolean done = false;
    boolean doneTwo = false;

		while (!done)
		{
			try
			{

				System.out.println("\nEnter number 0-6 for today's day");
		    NumToday = scanner.nextInt();
				done = true;
		   }
		  catch(InputMismatchException e)
		{
				scanner.nextLine();
				System.out.println("You may only enter a digit 0-6 ");
				System.out.println("Please try again");
		}
	}

    // Run the same loop, but for the second question. I changed the boolean
    // but the rest is unchanged

      while (!doneTwo)
      {
        try
        {

          System.out.println("\nEnter number 0-6 for the future day");
          NumFuture = scanner.nextInt();
          doneTwo = true;
         }
        catch(InputMismatchException e)
      {
          scanner.nextLine();
          System.out.println("You may only enter a digit 0-6 ");
          System.out.println("Please try again");
      }
}
}
}
