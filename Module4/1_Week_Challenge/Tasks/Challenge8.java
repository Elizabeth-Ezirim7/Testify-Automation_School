import java.util.Arrays;

public class Challenge8 {
    public static void main(String[] args) {
        int[] arr = {4, 2, 7, 9, 3, 6, 1, 5, 8, 2, 7, 1, 9, 3, 6, 1, 5, 8};
        countingSort(arr);

        System.out.println("Sorted array: " + Arrays.toString(arr));
    }

    private static void countingSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        int min = Arrays.stream(arr).min().getAsInt();
        int range = max - min + 1;

        int[] count = new int[range];
        int[] output = new int[arr.length];

        for (int value : arr) {
            count[value - min]++;
        }

        for (int i = 1; i < range; i++) {
            count[i] += count[i - 1];
        }

        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[arr[i] - min] - 1] = arr[i];
            count[arr[i] - min]--;
        }

        System.arraycopy(output, 0, arr, 0, arr.length);
    }
}
