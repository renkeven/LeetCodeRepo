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
        current_win = 0
        running_set = []
        
        for i in s:
            if i not in running_set:
                running_set.append(i)
                current_win += 1
            else:
                max_win = max(max_win, current_win)
                running_set.append(i)
                running_set = running_set[running_set.index(i) + 1:]
                current_win = len(running_set)
                        
        return max(current_win, max_win)