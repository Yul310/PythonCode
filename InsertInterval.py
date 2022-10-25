class Solution(object):
    def insert(self, intervals, newInterval):



        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        result = []
        for interval in intervals:
            # print(result)
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
                
        return result




        # newlist = []
    
#         if intervals == []:
#             return [newInterval]
            
#         elif intervals[0][0] > newInterval[0] and intervals[0][0] > newInterval[1]:
       
#            newlist.append(newInterval)
         
#         elif intervals[len(intervals)-1][0] < newInterval[0]:
            
#             newlist.append(newInterval) 
            

        
        
        
#         for i in range(0,len(intervals)):
#             # print(newInterval)
#             # print(intervals[i])
            
            
            
            
#             if (intervals[i][0] <= newInterval[0]) and (intervals[i][1] >= newInterval[0]):
#                 # print("hh")
#                 intervals[i][0] = min(intervals[i][0],newInterval[0])
#                 intervals[i][1] = max(intervals[i][1],newInterval[1])
#                 if newInterval in newlist:
#                     location = newlist.index(newInterval)
#                     newlist.pop(location)
#                 newInterval = [intervals[i][0],intervals[i][1]]
#                 newlist.append(newInterval)
                
#             elif (intervals[i][0] <= newInterval[1]) and (intervals[i][1] >= newInterval[1]):
#                 # print("tt")
#                 intervals[i][0] = min(intervals[i][0],newInterval[0])
#                 intervals[i][1] = max(intervals[i][1],newInterval[1])
#                 if newInterval in newlist:
#                     location = newlist.index(newInterval)
#                     newlist.pop(location)
#                 newInterval = [intervals[i][0],intervals[i][1]]
#                 newlist.append(newInterval)
                
#             elif (intervals[i][0] >= newInterval[0]) and (intervals[i][1] <= newInterval[1]):
#                 # print("pass")
#                 if newInterval not in newlist:
                 
#                     newlist.append(newInterval)
#                 continue
                
                
#             elif i+1 < len(intervals):
#                 if (intervals[i][1] < newInterval[0]) and (intervals[i+1][0] > newInterval[1]):
#                     # print("between")
#                     newlist.append([intervals[i][0],intervals[i][1]])
#                     newlist.append(newInterval) 
#                 else:
#                     # print("nono")
#                     newlist.append([intervals[i][0],intervals[i][1]])
                    
#             else:
#                 # print("nono")
#                 newlist.append([intervals[i][0],intervals[i][1]])
                
         
#             newlist.sort(key=lambda x:x[0])  
            
#         return newlist
