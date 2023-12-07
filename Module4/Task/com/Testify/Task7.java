package com.Testify;

import java.lang.reflect.Array;
import java.util.Arrays;

//User
//create a two dimensional array with 4 rows and 3 columns.Fill only the first column with any fruits of your choice.
public class Task7 {
    public static void main(String[] args) {
        String[][] fruits = new String[4][3];
        fruits[0][0] = "Carrot";
        fruits[1][0] = "Banana";
        fruits[2][0] = "BeetRoot";
        fruits[3][0] = "Orange";
        System.out.println(fruits[1][0] + "is my favorite fruit" );

    }
}
