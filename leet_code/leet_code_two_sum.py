def twoSum(nums: list[int], target: int) -> list[int]:
    cache = {}
    for idx, num in enumerate(nums):
        search_num = target - num

        if search_num in cache:
            return [cache[search_num], idx]
        cache[num] = idx
    return []


def maxProfit(prices: list[int]) -> int:
    profits = {}
    for idx, price in enumerate(prices):
        profit = max(prices[idx:]) - price
        if profit > profits.get(price, -1):
            profits[price] = profit
    return max(profits.values())


class Solution:
    def max_profit(self, price: list[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(price):
            current_profit = price[sell] - price[buy]
            if price[buy] < price[sell]:
                max_profit = max(current_profit, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit

    def maxProfitNonWorking(self, prices: list[int]) -> int:
        profits = {}
        max_num = {}
        for idx, price in enumerate(prices):
            if idx >= max_num.get("idx", 0):
                max_num["max"] = max(prices[idx:])
                max_num["idx"] = prices.index(max_num["max"])
            profit = max_num["max"] - price
            if profit > profits.get(price, -1):
                profits[price] = profit
        return max(profits.values())


# 10 20 30 12 32
def productExceptSelf(nums: list[int]) -> list[int]:
    answer = []
    preproduct = 1
    postproduct = 1
    for idx, num in enumerate(nums):
        answer.append(preproduct)
        preproduct *= num
    print(answer)
    for idx in range(len(nums) - 1, -1, -1):
        answer[idx] *= postproduct
        postproduct *= nums[idx]
    return answer


# resp = productExceptSelf([1, 2, 3, 4])
#
# print(resp, "-----", [1, 2, 3, 4])


def insertinterval(intervals, new_interval: list[int]) -> list[int]:
    for idx in range(len(intervals)):
        current_interval = intervals[idx]
        if (
            current_interval[0] <= new_interval[0]
            and current_interval[1] >= new_interval[0]
        ):
            updated_interval = [
                min(current_interval[0], new_interval[0]),
                max(current_interval[1], new_interval[1]),
            ]
            intervals[idx] = updated_interval
    print(intervals)
    return intervals


def insertinterval1(intervals, new_interval):
    start_ind = 0
    while not intervals[start_ind][0] >= new_interval[0] and start_ind < len(intervals):
        start_ind += 1
    start_ind -= 1

    end_ind = start_ind
    while not intervals[end_ind][1] <= new_interval[1]:
        end_ind += 1
    print(start_ind, end_ind - 1)


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newinterval = [4, 8]
# insertinterval([[1, 3], [6, 9]], [2, 5])
insertinterval1(intervals, newinterval)
