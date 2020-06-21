import java.util.*;
public class Fibonacci4 {

    public static void main(String[] args) {

        int range, firstNum, secondNum, sum;
        String oddNums;
        range = 100;
        firstNum = 0;
        secondNum = 1;
        List<Integer> list = new ArrayList<Integer>();
        //List<Integer> a[] = new ArrayList<Integer>();
        int a[]={1,2,5,6,3,2};

        while (firstNum <= range)
        {

            sum = firstNum + secondNum;
            firstNum = secondNum;
            secondNum = sum;
            list.add(firstNum);


        }

        for(int i=0;i<list.length;i++){

        if(list[i]%2!=0){

        System.out.println(list[i]);
        }
        }
    }
}
