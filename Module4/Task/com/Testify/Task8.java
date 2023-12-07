package com.Testify;

import java.util.Scanner;

//Interest Calculator
public class Task8 {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Enter principal amount");
        double principal = userInput.nextDouble();

        System.out.println("Enter interest rate");
        double rate = userInput.nextDouble();
        //rate /= 100;

        System.out.println("Enter time in years");
        double time = userInput.nextDouble();

        double simpleInterest = (principal * rate * time) / 100;
        System.out.println("Your Simple Interest is " + simpleInterest);
    }


}
