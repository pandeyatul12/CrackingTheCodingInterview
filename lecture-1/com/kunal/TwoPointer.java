package com.kunal;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TwoPointer {
    public static void main(String[] args) {
        // Try yourself

        // find triplet with sum 0
    }

    public static List<List<Integer>> triplet(int[] arr) {
        List<List<Integer>> triplets = new ArrayList<>();

        Arrays.sort(arr);

        for (int i = 0; i < arr.length; i++) {

            if(i > 0 && arr[i] == arr[i-1]) {
                continue;
            }

            search(arr, -arr[i], i+1, triplets);
        }
        
        return triplets;
    }

    // find pair with target sum
    private static void search(int[] arr, int target, int start, List<List<Integer>> triplets) {
        // try yourself
    }

}
