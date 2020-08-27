Ska "class Student extends PersonB" vara innanför {} för PersonB

package learn;

 class PersonB {// PersonB is the superclass
	String name;
	String address;
	String email;
	String phoneNumber;
	
	
	PersonB(String name, String address, String email, String phoneNumber ) {
		this.name = name;
		this.address = address;
		this.email = email;
		this.phoneNumber = phoneNumber;
	}
	
	public String toString() {
		return name + ", " + address + ", " + email + ", " + phoneNumber;
	}
	
	class Student extends PersonB {  // Student is a subclass of Person
		String classYear;
		  public static void student() {//main(String[] args) {
			  System.out.println("I'm a student class");
		  }
	}
		}
