import java.util.*;

public class Main {

    public static void main(String[] args) {

        int[] arr = { 7, 5, 9, 0, 3, 1, 2, 4, 6, 8 };
        int len = arr.length;

        for (int i = 1; i < len; i++) {

            for (int j = i; j > 0; j--) {

                if (arr[j - 1] > arr[j]) {
                    // 스와프
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                }

                else break;
            }

        }

        for (int i = 0; i < len; i++) {
            System.out.print(arr[i] + " ");
        }

        System.out.println();
    }

}
