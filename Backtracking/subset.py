
#Iterate through all possible subsets of a given set of numbers using backtracking.
def backtrack(start, path):

    # 1. Record current state
    result.append(path[:])

    # 2. Try choices
    for i in range(start, len(nums)):

        # Choose
        path.append(nums[i])

        # Explore
        backtrack(i + 1, path)

        # Undo
        path.pop()

#DFS approach to generate all subsets of a given set of numbers.
def subsets(nums):
    result = []
    def dfs(index, path):
        if index == len(nums):
            result.append(path[:])
            return

        # Include the current number
        path.append(nums[index])
        dfs(index + 1, path)
        
        # Exclude the current number
        path.pop()
        dfs(index + 1, path)

    dfs(0, [])
    return result


print(subsets([1, 2,3,4]))