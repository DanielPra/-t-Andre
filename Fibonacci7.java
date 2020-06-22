import java.util.*;
public class Fibonacci7 {

    public static void main(String[] args) {

        int range, firstNum, secondNum, sum;
        String oddNums;
        range = 1000;
        firstNum = 0;
        secondNum = 1;
        List<Integer> list = new ArrayList<Integer>();


        System.out.print("Fibonaccital 1 - 1000: ");

        while (secondNum <= range)
            {

                System.out.print(firstNum + ", ");

                sum = firstNum + secondNum;
                firstNum = secondNum;
                secondNum = sum;
                list.add(firstNum);


            }

        int oddSum = 0;
        for(int n : list) {
            if(n % 2 != 0) {
                oddSum += n;
                
            }
        }
        //Prints out sum of all the odd numbers
        System.out.println("\nThe sum of the odd numbers are " + oddSum);
    }
}
