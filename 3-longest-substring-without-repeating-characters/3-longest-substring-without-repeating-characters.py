class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        improving on previous shit solution
        start on character, expand window until you hit a duplicate. record dupe, start on next         char and go until you hit the end.
        
        tested with sets, looks like array is best
        """
        
        if len(s) < 2:
            return len(s)

        max_win = 0
        running_set = []
        
        for i in s:
            if i in running_set:
                max_win = max(max_win, len(running_set))
                running_set = running_set[running_set.index(i) + 1:]
            running_set.append(i)
            
        return max(max_win, len(running_set))