class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        totalGas = 0
        res = 0
        for i in range(len(gas)):
            totalGas += (gas[i] - cost[i])
            if totalGas < 0: # oh well it did not work out
                totalGas = 0
                res = i + 1
        return res