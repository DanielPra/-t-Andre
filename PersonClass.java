class Student extends Person {  // Student is a subclass of Person
	String classYear;
	  public static void student() {//main(String[] args) {
		  System.out.println("I'm a student class");
	  }
}

class Employee extends Person {  // Employee is the subclass of Person
	static int salary;
	int dateHired;
	  public static void employee() {
		  salary = 30000;
		  System.out.println("The employee salary is " + salary);
	  }
}

class Faculty extends Employee {
	String officeHours;
	String rank;
	  public static void faculty() {
		  System.out.println("Faculty class");
}
}
