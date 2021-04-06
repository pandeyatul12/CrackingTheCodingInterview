def orderAgnosticBinarySearch(nums, target):
    s, e = 0, len(nums) - 1

    isAsc = nums[s] < nums[e] # True or False

    while s <= e:

        # middle
        m = s + (e - s) // 2

        if nums[m] == target:
            return m

        if isAsc:
            if target < nums[m]:
                e = m - 1
            else:
                s = m + 1
        else:
            if target > nums[m]:
                e = m - 1
            else:
                s = m + 1

    return -1


# Q2: Ceiling of a number
# Q3: Floor of a number

# Q4: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums, target):
        ans = [-1, -1]

        ans[0] = self.bs(nums, target, False)

        if ans[0] != -1:
            ans[1] = self.bs(nums, target, True)

        return ans

    def bs(self, nums, target, checkRight):
        index = -1
        s, e = 0, len(nums) - 1

        while s <= e:

            m = s + (e - s) // 2
            if target < nums[m]:
                e = m - 1
            elif target > nums[m]:
                s = m + 1
            else: # target == nums[m]
                index = m
                if checkRight:
                    s = m + 1
                else:
                    e = m - 1
        return index


# https://leetcode.com/problems/peak-index-in-a-mountain-array/
class Solution:
    def peakIndexInMountainArray(self, arr):
        s, e = 0, len(arr) - 1
        while s < e:
            m = s + (e - s) // 2
            if arr[m] > arr[m + 1]:
                e = m
            else:
                s = m + 1
        # here s == e
        return e

# https://leetcode.com/problems/search-in-rotated-sorted-array/
def pbs(arr, target):
    pivot = findPivot(arr, 0, len(arr) - 1)

    # array is not rotated at all
    # just do normal binary search
    if pivot == -1:
        return bs(arr,  0, len(arr) - 1, target)

    if arr[pivot] == target:
        return pivot

    if arr[0] <= target:
        return bs(arr, 0, pivot-1, target)

    return bs(arr, pivot + 1, len(arr)-1, target)

def bs(arr, s, e, target):
    # do this one yourself: just normal binary search
    pass

def findPivot(arr, s, e):
    if e < s:
        return -1

    if e == s:
        return e

    m = s + (e - s) // 2

    if m < e and arr[m] > arr[m+1]:
        return m
    if m > s and arr[m] < arr[m-1]:
        return m-1

    if arr[s] >= arr[m]:
        return findPivot(arr, s, m-1)

    return findPivot(arr, m+1, e)

# Put it in just one function: HOMEWORK
