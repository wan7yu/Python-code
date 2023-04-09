"""
给一个非空字符串 s，你最多可以删除一个字符。判断是否可以把它变成回文串。

给定的字符串只包含小写字母
字符串的长度最大为 50000
样例
样例 1:

输入: s = "aba"
输出: true
解释: 原本就是回文串
样例 2:

输入: s = "abca"
输出: true
解释: 删除 'b' 或 'c'
样例 3:

输入: s = "abc"
输出: false
解释: 删除任何一个字符都不能使之变成回文串
"""


class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def equals(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def valid_palindrome(self, s: str) -> bool:
        # Write your code here
        length = len(s)
        start, end = 0, length-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.equals(s, start+1, end) or self.equals(s, start, end-1)
        return True
