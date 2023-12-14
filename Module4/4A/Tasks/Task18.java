package Tasks;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Task18 {
    public static void main(String[] args) {
        try {
            Scanner userInput = new Scanner(System.in);
            System.out.print("Enter your Age: ");
            int age = userInput.nextInt();
            System.out.println("This is your age: " + age);
            userInput.close();
        } catch (InputMismatchException dataTypeException){
            System.out.println("Invalid age input");
            System.out.println(dataTypeException);

        }

    }
}