public class Main {

    // 순차 탐색 알고리즘
    public static int sequantialSearch(int[] arr, int len, int target) {
        // 각 원소를 하나씩 확인하며
        for (int i = 0; i < len; i++) {
            // 현재의 원소가 찾고자 하는 원소와 동일한 경우
            if (arr[i] == target) {
                return i; 
            }
        }
        return -1; // 원소를 찾지 못한 경우 -1 반환
    }

    public static void main(String[] args) {

        int[] arr = {3, 5, 2, 4, 9};
        int idx;

        idx = sequantialSearch(arr, arr.length, 5);

        // 순차 탐색 수행 결과 출력
        if (idx == -1) {
            System.out.println("탐색 실패!");
        } else {
            System.out.println("타겟 저장 인덱스: " + idx);
        }

    }

}
