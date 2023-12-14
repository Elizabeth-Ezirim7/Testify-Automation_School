package Tasks.Task12.Task12B;

import Tasks.Task12.Task12A.FirstClass;

public class SecondClass {
    public static void main(String[] args) {
        FirstClass access = new FirstClass();
        access.firstClassMethod();

        SecondClass secondAccess = new SecondClass();
        secondAccess.secondClassMethod();
    }

    private void secondClassMethod(){
        System.out.println("This method is accessible only in this class");

    }
}
