"""
415 · 有效回文串
给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，并忽略大小写。

你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。

在这个题目中，我们将空字符串判定为有效回文。

样例
样例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释: "amanaplanacanalpanama"
样例 2:

输入: "race a car"
输出: false
解释: "raceacar"
样例 3:

输入: "1b , 1"
输出: true
解释: "1b1"
挑战
O(n) 时间复杂度，且不占用额外空间
"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def is_palindrome(self, s: str) -> bool:
        # write your code here
        s = s.lower()
        length = len(s)
        p1, p2 = 0, length-1
        while p1 < p2:
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
