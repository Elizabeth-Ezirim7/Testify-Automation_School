package Tasks;

//User
//create a two dimensional array with 4 rows and 3 columns.Fill only the first column with any fruits of your choice.
public class Task7 {
    public static void main(String[] args) {
        String[][] fruits = new String[4][3];
        fruits[0][0] = "Carrot";
        fruits[1][0] = "Banana";
        fruits[2][0] = "Mango";
        fruits[3][0] = "Orange";
        //System.out.println(fruits[1][0] + " is my favorite fruit" );
        System.out.println("2D Array with Fruits:");
        fruitArray(fruits);

    }

    public static void fruitArray(String[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.print(array[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
