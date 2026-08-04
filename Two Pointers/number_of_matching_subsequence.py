class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        seen = {}

        for word in words:
            if word in seen:
                count += seen[word]   # True -> 1, False -> 0
                continue

            if not word:
                seen[word] = True
                count += 1
                continue

            str_read = 0
            word_read = 0

            while str_read < len(s) and word_read < len(word):
                if s[str_read] == word[word_read]:
                    word_read += 1
                str_read += 1

            is_subsequence = (word_read == len(word))
            seen[word] = is_subsequence

            count += is_subsequence

        return count