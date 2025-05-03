import math
import sys

file = sys.argv[1]

with open(file, 'r') as f:
    list_nums = sorted(list(map(int, f.read().split())))


def counter_min_step_to_same_num(lst_nums: list[int]) -> int:

    med_num = lst_nums[len(lst_nums) // 2]
    count = 0
    for x in lst_nums:
        count += int(math.fabs(x - med_num))
    return count


if __name__ == '__main__':
    print(counter_min_step_to_same_num(list_nums))
