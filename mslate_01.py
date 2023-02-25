'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.

Sample:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

'''

from typing import List


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


class HouseRobber:
    '''
    Class to handle house robbing.
    '''

    nums = [2, 3, 5, 12, 13, 16]

    @classmethod
    def resolve_key(cls, value, data: dict):
        '''
        Method to find key by value in a given dictionary.
        '''
        for dict_key, dict_value in data.items():
            if value == dict_value:
                return dict_key

    @classmethod
    def create_pattern(cls, start, data_list: List[int]):
        '''
        Method to resolve the robbing pattern given a list of houses.
        '''
        res_list = []
        res_list.append(start)
        i = start+2
        while i < len(data_list):
            res_list.append(i)
            i = i+2

        return res_list

    @classmethod
    def robbing_pattern(cls, loot_list: List[int] = None):
        '''
        Method to find the most-profitable robbing pattern.
        '''
        if loot_list is None or len(loot_list) == 0:
            loot_list = cls.nums
        ## Since we are working with non-adjacent nodes, there can only be two patterns:
        ## one starting at index 0 and one starting at index 1, with both indices incrementing by 2.
        starts = [0, 1]
        loot_dict = {}

        for start in starts:
            i = start
            summary = 0
            while i < len(loot_list):
                summary = summary + loot_list[i]
                i = i+2
            loot_dict[start] = summary

        print(f"\nLoot dictionary: {loot_dict}")

        max_loot = max([loot_dict.get(0), loot_dict.get(1)])

        start = cls.resolve_key(max_loot, loot_dict)

        res_dict = {
            "starting_position": start,
            "total_loot": max_loot,
            "pattern (indices)": cls.create_pattern(start=start, data_list=loot_list)
        }
        return res_dict


def main():
    '''
    Main executable function for the page.
    '''
    inp_list = ConsoleInputHandler.input_array()
    sol = HouseRobber.robbing_pattern(inp_list)
    print(sol)


if __name__ == "__main__":
    main()
