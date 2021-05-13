from collections import defaultdict
from typing import List, Tuple
import copy as cp

def longest_substring(s: str) -> Tuple[str, int]:
    strng = None
    len_strng = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            new_str = s[i:j]
            for k in new_str:
                flag = 1
                if new_str.count(k) > 1:
                    flag = 0
                    break
            if len(new_str) > len_strng and flag == 1:
                strng = cp.deepcopy(new_str)
                len_strng = len(strng)
    return [strng, len_strng]

print(longest_substring("abcabcbb"))  # abc, 3
print(longest_substring("bbbbb"))  # b, 1
print(longest_substring("pwwkew"))  # wke, 3
# --------------------------------
def group_anagrams(words: List[str]) -> List[List[str]]:    
    temp = defaultdict(list)
    for ele in words:
        temp[str(sorted(ele))].append(ele)
    res = list(temp.values())
    return res

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) # [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

