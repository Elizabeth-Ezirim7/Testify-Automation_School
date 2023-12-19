package Tasks.Task19.Task19b;

public class Task19b2 {

    public static void main(String[] args) {
        // Accessing the static variable directly without creating an object of class A
        System.out.println("Shared value from class A in main method: " + Task19b1.sharedValue);

        // Modifying the static variable from class A
        Task19b1.sharedValue = 50;

        // Creating an object of class B
        Task19b2 secondObject = new Task19b2();
        // Calling a method in class B that prints the shared value
        secondObject.printSharedValue();
    }


    public void printSharedValue() {
        // Accessing the static variable from class A without creating an object
        System.out.println("Shared value from class A in class B: " + Task19b1.sharedValue);
    }

}

