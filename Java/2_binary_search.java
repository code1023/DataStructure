public class Main {

    // 이진 탐색 알고리즘
    public static int binarySearch(int[] arr, int len, int target) {
        
        int first = 0;
        int last = len - 1;
        int mid;

        while (first <= last) {
            mid = (first + last) / 2;

            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) return mid;

            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            else if (arr[mid] > target) last = mid - 1;

            // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else first = mid + 1;    
        }
        
        return -1;      // 없을 경우 -1 반환
                                            
    }

    public static void main(String[] args) {

        int[] arr = {1, 3, 5, 6, 7, 9, 11, 13, 17, 30};
        int idx;

        idx = binarySearch(arr, arr.length, 8);

        // 이진 탐색 수행 결과 출력
        if (idx == -1) {
            System.out.println("탐색 실패!");
        } else {
            System.out.println("타겟 저장 인덱스: " + idx);
        }

    }

}
