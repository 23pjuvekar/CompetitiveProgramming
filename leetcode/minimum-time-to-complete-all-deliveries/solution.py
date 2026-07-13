class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:

        d1, d2 = d
        r1, r2 = r

        def gcd(a, b):
            return math.gcd(a, b)

        def lcm(a, b):
            if a == 0 and b == 0:
                return 0
            return abs(a * b) // gcd(a, b)

        l = lcm(r1, r2)
            
        def complete(time):
            only_d1_slots = (time // r2) - (time // l)
            only_d2_slots = (time // r1) - (time // l)
            both_avaiable = time - (time // r1) - (time // r2) + (time // l)
            d1_needed_shared = max(0, d1 - only_d1_slots)
            d2_needed_shared = max(0, d2 - only_d2_slots)
            return d1_needed_shared + d2_needed_shared <= both_avaiable


        low = d1 + d2
        high = (d1 + d2) * (max(r1, r2))
        res = r

        while low <= high:
            mid = (low + high) // 2
            if complete(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
            


        """
        time = 0
        drones = [[d[0], r[0]], [d[1], r[1]]]
        completed_deliveries = 0
        total_deliveries = d[0] + d[1]
        drone_next_avaible = [0, 0]
        while completed_deliveries < total_deliveries:
            time += 1
            drone_1_avaible = drones[0][0] > 0 and (time % drones[0][1] != 0)
            drone_2_avaible = drones[1][0] > 0 and (time % drones[1][1] != 0)
            if drone_1_avaible and drone_2_avaible:
                if drones[0][0] > drones[1][0]:
                    drones[0][0] -= 1
                    completed_deliveries += 1
                elif drones[0][0] < drones[1][0]:
                    drones[1][0] -= 1
                    completed_deliveries += 1
                else:
                    if drones[0][1] < drones[0][1]:
                        drones[0][0] -= 1
                        completed_deliveries += 1
                    else:
                        drones[1][0] -= 1
                        completed_deliveries += 1
            elif drone_1_avaible:
                drones[0][0] -= 1
                completed_deliveries += 1
            elif drone_2_avaible:
                drones[1][0] -= 1
                completed_deliveries += 1
                
        return time
        """
