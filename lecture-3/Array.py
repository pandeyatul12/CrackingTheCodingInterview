class Reader:
    def __init__(self, nums):
        self.nums = nums

    def get(self, index):
        return self.nums[index]

if __name__ == '__main__':
    nums = Reader([1,2,3,3,4,5,6,8,9,10,11,13,14,15,17,18,19,20, 21, 23, 24, 25, 27, 28])
    print(nums.get(2))
