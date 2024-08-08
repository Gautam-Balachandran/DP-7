﻿# Time Complexity : O(m*n)
# Space Complexity : O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p:
            return False

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]

# Examples

# Example 1
solution = Solution()
result = solution.isMatch("aa", "a*")
print(result)  # Output: True

# Example 2
solution = Solution()
result = solution.isMatch("mississippi", "mis*is*p*.")
print(result)  # Output: False

# Example 3
solution = Solution()
result = solution.isMatch("ab", ".*")
print(result)  # Output: True