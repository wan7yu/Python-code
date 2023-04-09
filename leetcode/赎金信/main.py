"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
提示：
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote 和 magazine 由小写英文字母组成
"""


class Solution:
    """解法一:使用数组作为哈希表"""

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        hash = [0 for i in range(26)]
        for i in magazine:
            hash[ord(i) - ord('a')] += 1
        for j in ransomNote:
            if hash[ord(j) - ord('a')] == 0:
                return False
            else:
                hash[ord(j) - ord('a')] -= 1
        return True


# class Solution:
#     """解法二:使用defaultdict"""

#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:

#         from collections import defaultdict

#         hashmap = defaultdict(int)

#         for x in magazine:
#             hashmap[x] += 1

#         for x in ransomNote:
#             value = hashmap.get(x)
#             if value is None or value == 0:
#                 return False
#             else:
#                 hashmap[x] -= 1

#         return True


# class Solution(object):
#     """解法三:使用字典存储 ransomNote 中字母出现的次数 """

#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         hashmap = dict()
#         for s in ransomNote:
#             if s in hashmap:
#                 hashmap[s] += 1
#             else:
#                 hashmap[s] = 1

#         # check if the letter we need can be found in magazine
#         for l in magazine:
#             if l in hashmap:
#                 hashmap[l] -= 1

#         for key in hashmap:
#             if hashmap[key] > 0:
#                 return False

#         return True


# class Solution:
#     """解法四:collections.Counter()"""

#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         import collections
#         if len(ransomNote) > len(magazine):
#             return False
#         return not collections.Counter(ransomNote) - collections.Counter(magazine)
