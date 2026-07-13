class Solution:
    def maximumPoints(self, enemy_energies: list[int], current_energy: int) -> int:
        min_enemy_energy = min(enemy_energies)

        if current_energy < min_enemy_energy:
            return 0

        total_energy = current_energy + sum(enemy_energies) - min_enemy_energy
        return total_energy // min_enemy_energy
