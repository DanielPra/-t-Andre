import java.util.Scanner;
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;  

public class PizzaMain {
	public static void main(String[] args) {
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
		
		calcCost(pizzaSize, numToppings, typeToppings);
		
	}
	static void getDescription(String x, int y, String z) {  //getDescription(pizzaSize, numToppings, typeToppings);
		System.out.println("You picked a " + x + " pizza and " + y + " " + z + " topping(s)");
		
	}
	static void calcCost(String pizzaSize, double numToppings, String typeToppings) {  
		double basePrice;
		String size = "small";
		String size1 = "medium";
		if (pizzaSize.equals(size)) { basePrice = 10 + 3 * numToppings; 
		System.out.println("You ordered a small pizza with " + numToppings + " " + typeToppings + " topping(s). Your bill is " + basePrice + " kr");
		}
		else if (pizzaSize.equals(size1))  { basePrice = 15 + 2.5 * numToppings;
		System.out.println("You ordered a medium pizza with " + numToppings + " topping(s). Your bill is " + basePrice + " kr");
		}
		else { basePrice = 20 + 2 * numToppings; 
		System.out.println("You ordered a medium pizza with " + numToppings + " topping(s). Your bill is " + basePrice + " kr");
		 
		}
	
	}
	
}
