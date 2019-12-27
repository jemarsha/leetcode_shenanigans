class PowerSet:
    """Class to generate the power set."""

    def __init__(self):
        self.result = []

    def generate_power_set(self, nums):
        results = []
        self.dfs(sorted(nums), 0, [], results)
        return results

    def dfs(self, nums, index, path, res):
        res.append(path)
        # print(path)
        for i in range(index, len(nums)):
            # print(nums[i])
            self.dfs(nums, i + 1, path + [nums[i]], res)


if __name__ =="__main__":
    s = PowerSet()
    li = [1, 2, 3]
    print(s.generate_power_set(li))

#Recursion path with backtracking

#f(0) [1] 2 numbers left to loop through ,index/i= 0
#f(1) [1,2] 1 number left to loop through, index/i =1
#f(2) [1,2,3] 0 numbers left to loop through, index/i =2
#f(1) [1,3]  0 numbers now left for index/i= 1 so this function is completely done
#f(0) [2] 1 number left to loop through, index/i= 1 now for f(0) because we're in the same loop still as the first call
#f(1) [2,3] 0 numbers left to loop through, index/i = 1
#f(0) [3] 0 numbers left to loop through, index/i=2