class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        matched = 0

        # Match target from left to right
        while matched < len(target):
            idx = ord(target[matched]) - ord('a')

            if count[idx] == 0:
                break

            count[idx] -= 1
            matched += 1

        # Start from the rightmost position we can change
        i = matched - 1

        # If target couldn't be fully matched,
        # the mismatch position itself is also a candidate.
        if matched < len(target):
            i = matched

        while i >= 0:

            # If this character was consumed while matching,
            # put it back.
            if i < matched:
                idx = ord(target[i]) - ord('a')
                count[idx] += 1

            current = ord(target[i]) - ord('a')

            # Find smallest character > target[i]
            for candidate in range(current + 1, 26):
                if count[candidate] > 0:

                    count[candidate] -= 1

                    suffix = ''.join(
                        chr(j + ord('a')) * count[j]
                        for j in range(26)
                    )

                    return (
                        target[:i]
                        + chr(candidate + ord('a'))
                        + suffix
                    )

            i -= 1

        return ""