'''
Given an array of integers numbers sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Sample:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''
from typing import List


class OccurenceHandler:
    '''
    Class to handle the occurence of a target value in a list of integers.
    '''
    nums: List[int] = [5, 7, 7, 8, 8, 8, 8, 8, 10]
    target: int = 8

    def __init__(self, nums: List[int], target: int) -> None:
        '''
        Optional init method.
        '''
        self.nums = nums
        self.target = target

    @classmethod
    def search_for_target(cls, nums: List[int] = None, target: int = None) -> List[int]:
        '''
        Function to search for initial and last occurences of the target in a list.
        '''
        if nums is None or len(nums) == 0:
            nums = cls.nums
        if target is None:
            target = cls.target
        print(f"\nSearching for target {target} in list {nums}")

        i = 0
        j = len(nums)-1
        start = -1
        end = -1

        while i < j:
            if nums[i] == target:
                start = i
                break
            elif nums[i] != target:
                i = i + 1

        while j > i:
            if nums[j] == target:
                end = j
                break
            elif nums[j] != target:
                j = j - 1

        return [start, end]


class ConsoleInputHandler:
    '''
    Class to handle console inputs.
    '''

    @classmethod
    def input_array(cls) -> List[int]:
        '''
        Method to handle array/list input as string.
        '''
        inp_list = []
        inp = input("Please enter the elements of the array: ").split(" ")
        while " " in inp:
            inp = inp.replace(" ", "")
        for i in range(len(inp)):
            try:
                inp_list.append(int(inp[i]))
            except Exception as ex:
                print(f"ERROR: {ex}")
        inp_list.sort()
        return inp_list

    @classmethod
    def input_target(cls) -> int:
        '''
        Method to handle target input as string.
        '''
        inp = int(input("Please enter the target: "))
        return inp

    @classmethod
    def input_arguments(cls):
        '''
        Method to call all input methods.
        '''
        inp_list = cls.input_array()
        target = cls.input_target()

        return inp_list, target


def main():
    '''
    Main executable function for script.
    '''
    nums, target = ConsoleInputHandler.input_arguments()
    res = OccurenceHandler.search_for_target(nums=nums, target=target)
    print(
        f"\nThe target ({target}) can be found in indices: {res}\nin the given array ({nums})")


if __name__ == "__main__":
    main()
