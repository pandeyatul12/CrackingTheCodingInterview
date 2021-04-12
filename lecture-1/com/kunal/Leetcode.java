package com.kunal;

import java.util.HashMap;
import java.util.Map;
// https://leetcode.com/problems/longest-repeating-character-replacement/submissions/
public class Leetcode {
    public int characterReplacement(String s, int k) {
        int start = 0;
        int max = 0;
        int maxLen = 0;
        
        Map<Character, Integer> map = new HashMap<>();
        
        for (int end = 0; end < s.length(); end++) {
            char ch = s.charAt(end);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
            
            // of the repeating character
            maxLen = Math.max(maxLen, map.get(ch));
            
            // condition violated
            // size of box - maxRepeating Character in the box
            // = number of characters to be replaced
            if (end-start+1 - maxLen > k) {
                char first = s.charAt(start);
                map.put(first, map.get(first) - 1);
                start++;
            }
                
            max = Math.max(max, end-start+1);
        }
        return max;
    }
}