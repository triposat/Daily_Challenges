class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boat = 0
        while left <= right:
            ans = people[left]+people[right]
            if ans <= limit:
                boat += 1
                left += 1
                right -= 1
            else:
                boat += 1
                right -= 1
        return boat