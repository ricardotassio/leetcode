class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for idx, ch in enumerate(s):
            if ch not in seen:
                seen[ch] = [idx, 1]
            else:
                seen[ch][1] += 1

        result = float('inf')
        for idx, count in seen.values():
            if count == 1:
                result = min(result, idx)
        return result if result != float('inf') else -1