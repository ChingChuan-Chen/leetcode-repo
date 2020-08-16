"""
Implement the class UndergroundSystem that supports three methods:

1. checkIn(int id, string stationName, int t)

	A customer with id card equal to id, gets in the station stationName at time t.
	A customer can only be checked into one place at a time.

2. checkOut(int id, string stationName, int t)

	A customer with id card equal to id, gets out from the station stationName at time t.

3. getAverageTime(string startStation, string endStation) 

	Returns the average time to travel between the startStation and the endStation.
	The average time is computed from all the previous traveling from startStation to endStation that happened directly.
	Call to getAverageTime is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.

 
Example 1:
Input
[&quot;UndergroundSystem&quot;,&quot;checkIn&quot;,&quot;checkIn&quot;,&quot;checkIn&quot;,&quot;checkOut&quot;,&quot;checkOut&quot;,&quot;checkOut&quot;,&quot;getAverageTime&quot;,&quot;getAverageTime&quot;,&quot;checkIn&quot;,&quot;getAverageTime&quot;,&quot;checkOut&quot;,&quot;getAverageTime&quot;]
[[],[45,&quot;Leyton&quot;,3],[32,&quot;Paradise&quot;,8],[27,&quot;Leyton&quot;,10],[45,&quot;Waterloo&quot;,15],[27,&quot;Waterloo&quot;,20],[32,&quot;Cambridge&quot;,22],[&quot;Paradise&quot;,&quot;Cambridge&quot;],[&quot;Leyton&quot;,&quot;Waterloo&quot;],[10,&quot;Leyton&quot;,24],[&quot;Leyton&quot;,&quot;Waterloo&quot;],[10,&quot;Waterloo&quot;,38],[&quot;Leyton&quot;,&quot;Waterloo&quot;]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, &quot;Leyton&quot;, 3);
undergroundSystem.checkIn(32, &quot;Paradise&quot;, 8);
undergroundSystem.checkIn(27, &quot;Leyton&quot;, 10);
undergroundSystem.checkOut(45, &quot;Waterloo&quot;, 15);
undergroundSystem.checkOut(27, &quot;Waterloo&quot;, 20);
undergroundSystem.checkOut(32, &quot;Cambridge&quot;, 22);
undergroundSystem.getAverageTime(&quot;Paradise&quot;, &quot;Cambridge&quot;);       // return 14.00000. There was only one travel from &quot;Paradise&quot; (at time 8) to &quot;Cambridge&quot; (at time 22)
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Waterloo&quot;);          // return 11.00000. There were two travels from &quot;Leyton&quot; to &quot;Waterloo&quot;, a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
undergroundSystem.checkIn(10, &quot;Leyton&quot;, 24);
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Waterloo&quot;);          // return 11.00000
undergroundSystem.checkOut(10, &quot;Waterloo&quot;, 38);
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Waterloo&quot;);          // return 12.00000

Example 2:
Input
[&quot;UndergroundSystem&quot;,&quot;checkIn&quot;,&quot;checkOut&quot;,&quot;getAverageTime&quot;,&quot;checkIn&quot;,&quot;checkOut&quot;,&quot;getAverageTime&quot;,&quot;checkIn&quot;,&quot;checkOut&quot;,&quot;getAverageTime&quot;]
[[],[10,&quot;Leyton&quot;,3],[10,&quot;Paradise&quot;,8],[&quot;Leyton&quot;,&quot;Paradise&quot;],[5,&quot;Leyton&quot;,10],[5,&quot;Paradise&quot;,16],[&quot;Leyton&quot;,&quot;Paradise&quot;],[2,&quot;Leyton&quot;,21],[2,&quot;Paradise&quot;,30],[&quot;Leyton&quot;,&quot;Paradise&quot;]]

Output
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, &quot;Leyton&quot;, 3);
undergroundSystem.checkOut(10, &quot;Paradise&quot;, 8);
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Paradise&quot;); // return 5.00000
undergroundSystem.checkIn(5, &quot;Leyton&quot;, 10);
undergroundSystem.checkOut(5, &quot;Paradise&quot;, 16);
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Paradise&quot;); // return 5.50000
undergroundSystem.checkIn(2, &quot;Leyton&quot;, 21);
undergroundSystem.checkOut(2, &quot;Paradise&quot;, 30);
undergroundSystem.getAverageTime(&quot;Leyton&quot;, &quot;Paradise&quot;); // return 6.66667

 
Constraints:
	There will be at most 20000 operations.
	1 <= id, t <= 10^6
	All strings consist of uppercase, lowercase English letters and digits.
	1 <= stationName.length <= 10
	Answers within 10^-5 of the actual value will be accepted as correct.


"""
class UndergroundSystem:

    def __init__(self):
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        


# param_3 = obj.getAverageTime(startStation,endStation)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

