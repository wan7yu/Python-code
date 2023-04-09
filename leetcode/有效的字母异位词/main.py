"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
 
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
 
提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
"""


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         buckets = [0 for i in range(26)]
#         print(buckets)


# Solution.isAnagram()

def isAnagram(s: str, t: str) -> bool:
    buckets = [0 for i in range(26)]
    for i in s:
        buckets[ord(i) - ord('a')] += 1
    for j in t:
        buckets[ord(j)-ord('a')] -= 1
    if buckets == [0 for i in range(26)]:
        return True
    else:
        return False


print(isAnagram("anagram", "nagaram"))
