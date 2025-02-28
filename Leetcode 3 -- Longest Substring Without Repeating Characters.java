//Leetcode 3: Longest substring without repeating characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

//Method 1: 2 pointers
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set <Character> seen = new HashSet <Character> ();
        int left = 0;
        int answer = 0;
        
        for (int right = 0;right < s.length(); right++){
            while(seen.contains(s.charAt(right))){
                seen.remove(s.charAt(left));
                left++;
            }
            seen.add(s.charAt(right));
            answer = Math.max(answer, right - left + 1);
        }

        return answer;

    }
}

//time complexity: O(N)
//space complexity: O(1) since there's only 26 characters or 128 if using ASCII
