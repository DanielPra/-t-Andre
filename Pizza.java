// Var sätter man in getDescription
// Bör jag ändra xToppings till int?

class Pizza {
    String pizzaSize;  
    int numCheeseToppings;
    int numPepperoniToppings;
    int numHamToppings;
    
    public void setPizzaSize(String s) {
        pizzaSize = s;
    }
    
    public String getPizzaSize() {
        return pizzaSize;
    }
    
    public void setNumCheeseToppings(int s) {
        numCheeseToppings = s;
    }
    
    public int getNumCheeseToppings() {
        return numCheeseToppings;
    }
    
    public void setNumPepperoniToppings(int s) {
        numPepperoniToppings = s;
    }
    
    public int getNumPepperoniToppings() {
        return numPepperoniToppings;
    }
    public void setNumHamToppings(int s) {
    	numHamToppings = s;
    }
    public int getNumHamToppings() {
    	return numHamToppings;
    }
    public static void getDescription(String x, int y, String z) {  //getDescription(pizzaSize, numToppings, typeToppings);
		System.out.println("You picked a " + x + " pizza and " + y + " " + z + " topping(s)");
    }
    public static void calcCost(String pizzaSize, double numToppings, String typeToppings) {  
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


/* public void addTopping (String type, int num) {
    	String inputTop = "cheese";
    	int numToppings = 1;
        if (inputTop == "cheese") {
		    setNumCheeseToppings(numToppings);
		} else if (inputTop == "pepperoni") {
		    setNumPepperoniToppings(numToppings)
		} else if (inputTop == "ham") {
		
		}
    }*/
 
