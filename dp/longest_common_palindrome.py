# -*- coding: utf-8 -*-
# @Time : 2023/9/20 下午8:10

class Solution(object):

    def longest_common_palindrome(self, str1, str2):
        """
        Args:
            str1:
            str2:
        Returns:
        """
        if len(str1) == 0 or len(str2) == 0:
            return ""
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        # 获取str1中以每个元素为中心的最长回文子串
        palindrome_list = self.get_palindrome_list(str1)
        res = ''
        for palindrome in palindrome_list:
            if palindrome in str2 and len(palindrome) > len(res):
                res = palindrome
        return res

    def longest_common_palindrome_v2(self, str1, str2):
        """
        Args:
            str1:
            str2:
        Returns:
        """
        if len(str1) == 0 or len(str2) == 0:
            return ""
        # 获取str1中以每个元素为中心的最长回文子串
        str1_palindrome_list = self.get_palindrome_list(str1)
        str2_palindrome_list = self.get_palindrome_list(str2)
        common_palindrome_set = set(str1_palindrome_list) & set(str2_palindrome_list)
        res = ''
        for _palindrome in common_palindrome_set:
            if len(_palindrome) > len(res):
                res = _palindrome
        return res

    def longest_common_substring(self, str1, str2):
        """
        最长公共子串
        Args:
            str1:
            str2:
        Returns:
        """
        m, n = len(str1), len(str2)
        # dp[i][j]表示以str1的前i个字符结尾和以str2的前j个字符结尾的最长公共子串长度
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0  # 最长公共子串长度
        end_index = 0  # 最长公共子串的右边界【闭区间】

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_index = i - 1
                else:
                    dp[i][j] = 0

        return str1[end_index - max_len + 1: end_index + 1]

    def longest_palindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res

    def longest_palindrome_by_dp(self, s: str) -> str:
        str_len = len(s)
        # 如果字符小于2，直接返回
        if str_len < 2:
            return s
        b_i = 0  # 最长回文串的起始索引
        max_len = 1  # 最长回文串的长度
        # dp[i][j] 表示s[i : j]是否是回文串【闭区间】
        dp = [[False for _ in range(str_len)] for _ in range(str_len)]
        for _ in range(str_len):
            # 单个字符串是回文串
            dp[_][_] = True

        for j in range(1, str_len):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:  # 子串长度<=3【左右边界字符相等，一定是回文串】
                        dp[i][j] = True
                    else:  # 当边界两边的字符相等时，继续判断内层的字符是否相等[避免越界]
                        dp[i][j] = dp[i + 1][j - 1]
                # 对比所有的回文串，取出长度最大的，回文串的起始位置
                if dp[i][j] and (j - i + 1) > max_len:
                    b_i = i
                    max_len = j - i + 1
        return s[b_i: b_i + max_len]

    def get_palindrome_list(self, s):
        palindrome_list = []
        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            palindrome_list.append(s1)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            palindrome_list.append(s2)
        return palindrome_list

    def palindrome(self, s: str, l: int, r: int) -> str:
        # 防止索引越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 向两边展开
            l -= 1
            r += 1
        # 返回以 s[l] 和 s[r] 为中心的最长回文串
        return s[l+1:r]


if __name__ == '__main__':
    str1 = "abacdfgdcaba"
    str2 = "abacdgfdcaba"

    str1 = "abcbaba"
    str2 = "caba"

    str1 = "abc"
    str2 = "abcb"

    str1 = "caba"
    str2 = "abcbcaba"

    print(Solution().longest_common_palindrome(str1, str2))
    str1 = "abcdefaba"
    str2 = "aabcdefgaba"
    print(Solution().longest_common_palindrome(str1, str2))
    print(Solution().longest_common_palindrome_v2(str1, str2))

    print(Solution().longest_palindrome(str1))
    print(Solution().longest_palindrome_by_dp(str1))

    print(Solution().longest_common_substring(str1, str2))
