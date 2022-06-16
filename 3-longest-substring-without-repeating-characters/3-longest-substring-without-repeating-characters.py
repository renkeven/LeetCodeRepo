class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        improving on previous shit solution
        start on character, expand window until you hit a duplicate. record dupe, start on next         char and go until you hit the end.
        
        tested with sets, looks like array is best
        """
        
        if(len(s) == 0 or len(s) == 1):
            return len(s)
        
        running_total = 0
        running_list = []
        
        for i in s:
            if i in running_list:
                tally = len(running_list)
                if tally > running_total:
                    running_total = tally
                [running_list.pop(0) for _ in range(running_list.index(i) + 1)]
                
                # if running_list.index(i) == len(running_list) - 1:
                #     running_list = []
                # else:
                #     running_list = running_list[(running_list.index(i)+1):]
        
            running_list.append(i)
            
        if(len(running_list) > running_total):
            return len(running_list)
        else:       
            return running_total
        
#         if len(s) < 2:
#             return len(s)

#         max_win = 0
#         current_win = 0
#         running_set = []
        
#         for i in s:
#             if i not in running_set:
#                 running_set.append(i)
#                 current_win += 1
#             else:
#                 max_win = max(max_win, current_win)
#                 running_set.append(i)
#                 running_set = running_set[running_set.index(i) + 1:]
#                 current_win = len(running_set)
                        
#         return max(current_win, max_win)