class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target_count, curr_window_count = {}, {}
        for char in t:
            target_count[char] = target_count.get(char, 0) + 1
        have, need = 0, len(target_count)

        ans = float("inf"), None, None
        l = 0
        for r in range(len(s)):
            char = s[r]
            curr_window_count[char] = curr_window_count.get(char, 0) + 1

            if char in target_count and curr_window_count[char] == target_count[char]:
                have += 1

            while l <= r and have == need:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                left_char = s[l]
                curr_window_count[left_char] -= 1
                if left_char in target_count and curr_window_count[left_char] < target_count[left_char]:
                    have -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]