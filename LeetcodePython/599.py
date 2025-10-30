class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        list_1_map = {}

        for i in range(len(list1)):
            if list1[i] in list_1_map:
                continue
            list_1_map[list1[i]] = i
        
        res = []
        min_res = float("inf")
        for i in range(len(list2)):
            if list2[i] in list_1_map:
                if min_res > i + list_1_map[list2[i]]:
                    min_res = i + list_1_map[list2[i]]
                    res = [list2[i]]
                elif min_res == i + list_1_map[list2[i]]:
                    res.append(list2[i])
        return res