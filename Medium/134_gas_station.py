class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_index, cur_gas, n = 0, 0, len(gas)
        for i in range(2 * n):
            cur_gas += gas[i % n] - cost[i % n]
            if cur_gas < 0:
                cur_gas = 0
                start_index = i + 1
        return -1 if start_index > n else start_index