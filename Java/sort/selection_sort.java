import java.util.*;

public class Main {

    public static void main(String[] args) {

        int[] arr = { 7, 5, 9, 0, 3, 1, 2, 4, 6 };
        int len = arr.length;

        for (int i = 0; i < len; i++) {
            int min_idx = i;

            for (int j = i + 1; j < len; j++) {
                if (arr[min_idx] > arr[j]) {
                    min_idx = j;
                }
            }

            // 스와프
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i] + " ");
        }

        System.out.println();
    }

}
