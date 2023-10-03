class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(customers) for customers in accounts])