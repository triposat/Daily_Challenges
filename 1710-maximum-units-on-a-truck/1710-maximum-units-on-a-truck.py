############################## My First Approach...

# Time: O(nlogn)
# Space: O(n)

# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key=lambda x: x[1], reverse=True)
#         temp = 0
#         res = 0
#         for b in boxTypes:
#             prev = temp
#             if prev >= truckSize:
#                 break
#             temp += b[0]
#             if temp < truckSize:
#                 res += b[0]*b[1]
#             else:
#                 if (truckSize-prev) <= b[0]:
#                     res += (truckSize-prev)*b[1]
#                     return res
#         return res

######################## More Precisely written approach

# Time: O(nlogn)
# Space: O(n)

# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key=lambda x: -x[1])
#         res = 0
#         for box, units in boxTypes:
#             if truckSize > box:
#                 truckSize -= box
#                 res += (box*units)
#             else:
#                 res += (truckSize*units)
#                 return res
#         return res

########################## More Precise Approach 

# # Time: O(nlogn)
# # Space: O(n)
    
# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         boxTypes.sort(key=lambda x: -x[1])
#         res = 0
#         for box, units in boxTypes:
#             res += min(truckSize, box)*units
#             truckSize -= box
#             if truckSize <= 0:
#                 return res
#         return res

######################### Best Optimal Approach
# Time: O(n)
# Space: O(n)
# Counting Sort Techniques...
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        cntr = Counter()
        for box, units in boxTypes:
            cntr[units] += box
        temp = 1000
        res = 0
        while temp > 0:
            ans = min(truckSize, cntr[temp])
            res += (ans*temp)
            truckSize -= ans
            if truckSize <= 0:
                return res
            temp -= 1
        return res
            