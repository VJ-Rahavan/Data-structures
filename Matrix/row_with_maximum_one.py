# I iterate through each row and use sum(row) to count the number of 1s.
# I keep track of the maximum count and its row index.
# I update them only when I find a strictly larger count, which automatically keeps the first row in case of a tie.
# Time complexity is O(m × n) and space complexity is O(1).

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx = 0
        row = 0
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            if count > maxx:
                row = i
                maxx = count

        return [row, maxx]
