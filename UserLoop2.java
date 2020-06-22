
import java.util.Scanner; 
public class UserLoop2 {

public static void main(String[] args) {

    Scanner input = new Scanner(System.in);
    String answer;
    int num, start, end, i, rem, temp, counter=0;
    Scanner scanner = new Scanner(System.in);

    do{

    System.out.print("Enter the start number: ");
  	start = scanner.nextInt();
  	System.out.print("Enter the end number: ");
  	end = scanner.nextInt();
  	scanner.close();

  	//generate Armstrong numbers between start and end
  	for(i=start+1; i<end; i++)
  	{
  	   temp = i;
  	   num = 0;
  	   while(temp != 0)
  	   {
  		rem = temp%10;
  		num = num + rem*rem*rem;
  		temp = temp/10;
  	   }
  	   if(i == num)
  	   {
  		if(counter == 0)
  		{
  		   System.out.print("Armstrong Numbers Between "+start+" and "+end+": ");
  		}
  		   System.out.print(i + "  ");
  		   counter++;
  	   }

    System.out.println("\nDo you want to print another number? Yes / No: ");
    answer = scanner.next();
    }

    while (answer.equals("Yes"));
  }  // Matchar med fel hakparantes?

  }
  }
