public class Fibonacci3 {

    public static void main(String[] args) {

        int range, firstNum, secondNum, sum;
        range = 100;
        firstNum = 0;
        secondNum = 1;
        //String[] oddNums = {};
        //String[] oddNums = new String[10];
        //ArrayList<String> oddNums = new ArrayList<String>();


        while (firstNum <= range)
        {

            sum = firstNum + secondNum;
            firstNum = secondNum;
            secondNum = sum;

            if ((firstNum % 2) != 0);
              System.out.print(", " + firstNum );







            //  oddNums.add(mystring);
            //System.out.print("Odd numbers: " + firstNum );

        }
    }
}
