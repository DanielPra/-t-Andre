// Varför funkar det inte att jämföra strängar med (typeToppings == "pepperoni"). Minnesposition och inte innehåll (?)

import java.util.Scanner;
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;  

public class PizzaMain1 {
	public static void main(String[] args) {
		//Pizza pizza = new Pizza(); Behövs ej vid samma packet?
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");  
		LocalDateTime now = LocalDateTime.now();  
		System.out.println(dtf.format(now));  
		System.out.println("Welcome to the cafe LNU");
		
		System.out.println("Please enter size of your pizza [small, medium, or large]:");
		Scanner keyboard = new Scanner(System.in);
		String inputSize = keyboard.next();
		String pizzaSize = inputSize.toLowerCase();
	
		System.out.println("Please enter type of topping [cheese, pepperoni, ham]: pepperoni: ");
		String inputTop = keyboard.next();
		String typeToppings =  inputTop.toLowerCase();
		
		System.out.println("Please enter the number of toppings you want: ");
		int numToppings = keyboard.nextInt();
		keyboard.close();
		
	
		Pizza.calcCost(pizzaSize, numToppings, typeToppings);
		//Pizza.getDescription(pizzaSize, numToppings, typeToppings);
		
		
	}
	
}

	// Ändra så att vi har tre instansvariabler för fyllning som i Pizza.java
		
		/*if (typeToppings.equals("cheese")) {
			int numCheeseToppings = numToppings;
			//System.out.println(numCheeseToppings);	
		}
		else if (typeToppings.equals("pepperoni")) {
			int numPepperoniToppings = numToppings;
		}
		else if (typeToppings.equals("ham")) {
			int numHamToppings = numToppings;
			//.out.println(numHamToppings);	
		}*/
		
