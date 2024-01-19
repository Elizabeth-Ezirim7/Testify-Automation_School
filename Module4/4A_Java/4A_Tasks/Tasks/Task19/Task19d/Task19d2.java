package Tasks.Task19.Task19d;

import java.util.Scanner;

public class Task19d2 {
    public static void main(String[] args) {

        Task19d1 myObject = new Task19d1();

        // Get user input for the name
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String userProvidedName = scanner.nextLine();

        // Invoke the printName method with the user-provided name
        myObject.printName(userProvidedName);


        scanner.close();
    }


}
