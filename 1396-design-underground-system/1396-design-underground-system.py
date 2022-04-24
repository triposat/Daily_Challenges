from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.routeName = defaultdict(int)
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        ans = self.check.pop(id)
        route = (ans[0], stationName)
        self.routeName[route] += t-ans[1]
        self.routeCount[route] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routeName[route]/self.routeCount[route]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
