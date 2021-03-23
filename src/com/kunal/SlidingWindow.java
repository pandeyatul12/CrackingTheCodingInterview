package com.kunal;

public class SlidingWindow {

    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};
        System.out.println(maxSum(arr, 3));
    }

    public static int minWindowSum(int[] arr, int s) {
        int start = 0;
        int windowSum = 0;
        int size = Integer.MAX_VALUE;

        for (int end = 0; end < arr.length; end++) {
            windowSum += arr[end];

            // shrink the window
            while (windowSum >= s) {
                size = Math.min(size, end-start+1);
                windowSum -= arr[start];
                start++;
            }
        }
        return size == Integer.MAX_VALUE ? 0 : size;
    }

    public static int maxSum(int[] arr, int k) {
        int start = 0;
        int windowSum = 0;
        int max = 0;

        for (int end = 0; end < arr.length; end++) {
            windowSum += arr[end];

            // getting out of the window
            if (end >= k-1) {
                if (windowSum > max) {
                    max = windowSum;
                }
                // move start ahead
                windowSum -= arr[start];
                start++;
            }
        }

        return max;
    }
}
