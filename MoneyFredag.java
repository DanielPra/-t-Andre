class Money {
     int dollars, dollars2; 
	 int cents, cents2;
	

	Money(int newDollars, int newCents) {
		dollars = newDollars;
		cents = newCents;
		System.out.println("You got " + dollars + " dollars and " + cents + " cents");
	}
	
	Money(int newDollars) {
		dollars = newDollars;
		cents = 0; // Borde jag använda set()
		System.out.println("You got " + dollars + " dollars");
		System.out.println("You got " + cents + " cents");
		
		
	}
	Money() {
		System.out.println("My no arguments constructor");
		
		
	}
	public static Money add(Money m1, Money m2) {
	    Money m3 = new Money(m1.dollars + m2.dollars, m1.cents + m2.cents);
		System.out.println("If you add the two sums you get " + m3.dollars + " dollars and " + m3.cents + " cents"); 
        return m3; 
	}
	
	public Money subtract(Money other) {
	    Money m3 = new Money(dollars - other.dollars, cents - other.cents);
	    return m3;
	}
	
}
	

public class MoneyMain {
	public static void main(String[] args ) {
		// Using constructors
		Money myobject = new Money(1, 2);
		Money myobject2 = new Money(5);
		Money myobject3 = Money.add(myobject, myobject2);
	
	    Money m3
	}	
}
