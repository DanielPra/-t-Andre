import java.util.Scanner; 

public class UserLoop {

public static void main(String[] args) {

    Scanner input = new Scanner(System.in);
    String answer;
    int num, start, end, i, rem, temp, counter=0;
    Scanner scanner = new Scanner(System.in);

    do{
    System.out.print("\nEnter the start number: ");
    start = scanner.nextInt();
    System.out.print("\nYou picked " + start);
    

    System.out.println("\nDo you want to print another number? Yes / No: ");
    answer = scanner.next();
    }
    while (answer.equals("Yes"));





  }
}
