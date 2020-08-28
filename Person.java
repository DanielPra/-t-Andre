package learn;

 class Person {// Person is the superclass
	String name;
	String address;
	String email;
	String phoneNumber;
	
	
	Person(String name, String address, String email, String phoneNumber ) {
		this.name = name;
		this.address = address;
		this.email = email;
		this.phoneNumber = phoneNumber;
	}
	
	public String toString() {
		return name + ", " + address + ", " + email + ", " + phoneNumber;
	}
		}


// Problem

Alt 1:  // implicit-super-constructor-person-is-undefined

class Student extends Person {  // Student is a subclass of Person
	String classYear;
	  public static void student() {
		  System.out.println("I'm a student class");
	  }
}

Alt 2:

class Student extends Person {  Student(String name, String address, String email, String phoneNumber) {
		super(name, address, email, phoneNumber);
		// TODO Auto-generated constructor stub
	}
// Student is a subclass of Person
	String classYear;
	  public static void student() {
		  System.out.println("I'm a student class");
	  }
}
