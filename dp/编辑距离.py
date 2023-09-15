# -*- coding: utf-8 -*-
# @Time : 2023/9/15 下午9:10

class Solution(object):
    """
    给定两个字符串str1和str2，再给定三个整数ic，dc和rc，分别代表插入、删除和替换一个字符的代价，请输出将str1编辑成str2的最小代价。
    "abc","adc",5,3,2
    """
    def minEditCost(self , str1: str, str2: str, ic: int, dc: int, rc: int) -> int:
        """"""
        # 将str1转换为str2
        m = len(str1)
        n = len(str2)
        # dp[i][j]表示str1[0:i]与str2[0:j]之间的最小编辑距离
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):  # str2长度为0，只能删除
            dp[i][0] = dc * i

        for j in range(n + 1):  # str1为0，只能插入
            dp[0][j] = ic * j

        for i in range(1, m + 1):
            print('*' * 30)
            for j in range(1, n + 1):
                print(str1[i - 1], str2[j - 1])
                if str1[i - 1] == str2[j - 1]:  # 无需操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + ic,
                        dp[i - 1][j] + dc,
                        dp[i - 1][j - 1] + rc
                    )
        return dp[-1][-1]


if __name__ == '__main__':

    word1 = 'abc'
    word2 = 'adc'
    rst = Solution().minEditCost(word1, word2, 5,3,2)
    print(rst)
