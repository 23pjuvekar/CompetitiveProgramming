class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # 5 --> 4 --> (+1) 5 --> 1 --> (+3) 4 --> 1 --> (+2) 3
        # Energy: 1, 4, 3, 2 --> +6
        # Experence: 2, 6, 3, 1 --> +2
        res = 0
        currEnergy = initialEnergy
        currExperience = initialExperience
        for energy, experience in zip(energy, experience):
            if energy >= currEnergy:
                res += ((energy - currEnergy) + 1)
                currEnergy = energy + 1
            if experience >= currExperience:
                res += ((experience - currExperience) + 1)
                currExperience = experience + 1
            currEnergy -= energy
            currExperience += experience
        return res
