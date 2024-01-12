//Write a java code to check for the prime numbers between 1 - 100
public class Challenge4 {
    public static void main(String[] args) {
        int i, j, count;

        System.out.println("Prime numbers between 1 to 100 :");
        for (i = 2; i <= 100; i++) {
            count = 0;
            for (j = i; j >= 1; j--) {
                if (i % j == 0)
                    count = count + 1;
            }
            if (count == 2)
                System.out.print("" + i + " ");
        }
    }
}
