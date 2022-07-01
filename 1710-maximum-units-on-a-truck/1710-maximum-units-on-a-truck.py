class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        t=0
        ans=0
        print(boxTypes)
        for b in boxTypes:
            prev=t
            if prev>=truckSize:
                break
            t+=b[0]
            if t<truckSize:
                ans+=b[0]*b[1]
            else:
                if (truckSize-prev)<=b[0]:
                    ans+=(truckSize-prev)*b[1]
                    break
        return ans