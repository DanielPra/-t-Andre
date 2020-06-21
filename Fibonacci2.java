// TODO: The program should also compute and print a sum of
// the odd-valued terms in the required Fibonacci sequence

// Lägg ihop alla ojämna tal


public class Fibonacci2 {

    public static void main(String[] args) {

        int range, firstNum, secondNum, sum;
        range = 100;
        firstNum = 0;
        secondNum = 1;
        //String[] oddNums = {};
        //String[] oddNums = new String[10];
        //ArrayList<String> oddNums = new ArrayList<String>();




        System.out.print("Upp till 100: ");

        while (firstNum <= range)
        {
            System.out.print(firstNum + ", ");

            sum = firstNum + secondNum;
            firstNum = secondNum;
            secondNum = sum;

            // TODO: The program should also compute and print a sum of
            // the odd-valued terms

          //  if ((firstNum % 2) != 0);
            //  oddNums.add(mystring);
              //System.out.print("Odd numbers: " + mystring );



        }
    }
}
