// Jag vill skriva ett program som tar ett tresiffrigt tal och gör om det till
// Tre ensiffriga tal. T.ex 123 -> 1, 2, 3 och gärna a = 1, b = 2, c = 3

import java.util.Scanner;
public class SplitNum
{

  public static void main(String[] args) {

  int num;

  Scanner scanner = new Scanner(System.in);
  System.out.print("Enter any number:");
  num = scanner.nextInt();

  while (num > 0) {

      System.out.println( num % 10);

      num = num / 10; // Skalar vi bort en siffra per loop?
                      // dvs 1234 -> 123 -> 12 -> 1

}
}
}
