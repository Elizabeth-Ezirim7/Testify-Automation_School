package Tasks.Task12.Task12A;

import Tasks.Task12.Task12B.SecondClass;

public class FirstClass {
    public static void main(String[] args) {
        FirstClass access = new FirstClass();
        access.firstClassMethod();


        //This is to test if the private access modifier can be accessed in another class/package
        //SecondClass secondAccess = new SecondClass();
        //secondAccess.secondClassMethod();

    }

    public void firstClassMethod(){
        System.out.println("This method is accessible everywhere");
    }
}
