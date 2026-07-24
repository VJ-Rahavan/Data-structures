class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        res = [0] * len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1] - i
            
            stack.append(i)
        
        return res


# "I traverse from right to left because the answer depends on future days. "
# "I maintain a monotonic decreasing stack of indices, "
# "where the temperatures at those indices are strictly increasing from the top of the stack outward. "
# "Before processing the current day, I remove all days that aren't warmer than the current temperature. "
# "The remaining top of the stack, if any, is the nearest warmer day, so the answer is the difference in indices. "
# " Each index is pushed and popped at most once, giving O(n) time complexity."

#Left to Right Approach
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
        
        return res

#Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(sol.dailyTemperatures([30, 40, 50, 60]))                  # Output: [1, 1, 1, 0]
    print(sol.dailyTemperatures([30, 60, 90]))                      # Output: [1, 1, 0]
    print(sol.dailyTemperatures([90, 80, 70]))                      # Output: [0, 0, 0]