class Solution:
   def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
       res = [0] * numberOfUsers
       off_map = {}
       
       events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
       
       for type, time, ids_string in events:
           time = int(time)
           
           if type == "MESSAGE":
               ids = ids_string.split(" ")
               for id_str in ids:
                   if id_str == "HERE":
                       for i in range(numberOfUsers):
                           if i not in off_map or off_map[i] <= time:
                               res[i] += 1
                   elif id_str == "ALL":
                       for i in range(numberOfUsers):
                           res[i] += 1
                   else:
                       id = int(id_str[2:])
                       res[id] += 1
                           
           elif type == "OFFLINE":
               id = int(ids_string)
               off_map[id] = time + 60
       
       return res
