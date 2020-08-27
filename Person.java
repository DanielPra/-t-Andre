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
