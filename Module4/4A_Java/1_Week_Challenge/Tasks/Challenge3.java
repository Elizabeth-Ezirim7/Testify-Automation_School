//Find 2 numbers of which the product is the maximum in an array

public class Challenge3 {
    public static void main(String[] args) {
        int[] array = {10, 5, 6, 9};
        Challenge3 maxNumber = new Challenge3();
        maxNumber.findTwoMaxNumbers(array);

    }

    public void findTwoMaxNumbers(int[] array) {
        int maxOne = 0;
        int maxTwo = 0;
        for (int num : array) {
            if (maxOne < num) {
                maxTwo = maxOne;
                maxOne = num;
            } else if (maxTwo < num) {
                maxTwo = num;
            }
        }
        System.out.println("First Max Number: " + maxOne);
        System.out.println("Second Max Number: " + maxTwo);
    }

}


