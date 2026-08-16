class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        s1Count = [0]* 26
        windowCount = [0] * 26

        for i in range(len1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] +=1

        if s1Count == windowCount:
            return True

        for i in range(len1, len2):
            windowCount[ord(s2[i]) - ord('a')] += 1
            windowCount[ord(s2[i - len1]) - ord('a')] -= 1

            if s1Count == windowCount:
                return True

        return False
