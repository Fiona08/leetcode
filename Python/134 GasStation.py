#134


# Time:  O(n)
# Space: O(1)


# There are N gas stations along a circular route, 
# where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and 
# it costs cost[i] of gas to travel from station i 
# to its next station (i+1). You begin the journey 
# with an empty tank at one of the gas stations.
# Return the starting gas station's index
# if you can travel around the circuit once, 
# otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.


class greedySol():
    def gasStation(self,gas,cost):
        start_station,diff_by_far,diff_total=0,0,0
        for i in range(len(gas)):
            diff_by_far+=gas[i]-cost[i]
            diff_total+=gas[i]-cost[i]
            if diff_by_far<0:
                diff_by_far=0
                start_station=i+1
        if diff_total<0:
            return -1
        return start_station
