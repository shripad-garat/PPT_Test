"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.

Note: Create a GitHub file for the solution and add the file link the the answer section below.
"""

def FirstUnique(s):
    try:

        for i in range(len(s)):
            if s[i] not in s[i+1:]:
                if s[i] not in s[:i] or i==0:
                    return i
        return -1

    except Exception as e:
        raise e
    
s = "loveleetcode"
print(FirstUnique(s=s))
s = "aabbccddaabc"
print(FirstUnique(s=s))