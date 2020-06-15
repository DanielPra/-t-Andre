import java.util.Scanner;

public class Undantag {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int pin, entry, x;
        String expectedPassword = "abc";
        String passwordEntry;
        x = 1;

        do{
        try{

        pin = 123;

        System.out.println("WELCOME TO THE BANK OF JAVA.");
        System.out.print("ENTER YOUR PIN: ");
        entry = keyboard.nextInt();

        while (entry != pin) {
            System.out.println("\nINCORRECT PIN. TRY AGAIN.");
            System.out.print("ENTER YOUR PIN: ");
            entry = keyboard.nextInt();
        }

        System.out.println("\nPIN ACCEPTED. YOUR ACCOUNT BALANCE IS $425.17");
        x = 2;
      }
  
      catch(Exception e){

      while(x==1);

}
