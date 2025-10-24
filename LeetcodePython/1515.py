class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        num_positions = len(positions)
        if num_positions == 0:
            return 0.0
        def calculate_total_distance(px: float, py: float) -> float:
            total_dist_sum = 0.0
            for x_pos, y_pos in positions:
                total_dist_sum += math.sqrt((px - x_pos)**2 + (py - y_pos)**2)
            return total_dist_sum
        current_x = sum(p[0] for p in positions) / num_positions
        current_y = sum(p[1] for p in positions) / num_positions
        min_total_distance = calculate_total_distance(current_x, current_y)
        chg = 100.0 
        while chg > 1e-6:
            found_better_in_step = False
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                next_x = current_x + chg * dx
                next_y = current_y + chg * dy
                dist_at_next_point = calculate_total_distance(next_x, next_y)
                if dist_at_next_point < min_total_distance: 
                    min_total_distance = dist_at_next_point
                    current_x, current_y = next_x, next_y
                    found_better_in_step = True
                    break 
            if not found_better_in_step:
                chg /= 2.0
                
        return min_total_distance