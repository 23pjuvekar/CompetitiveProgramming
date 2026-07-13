class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        test_devices = 0

        for battery in batteryPercentages:
            if battery - test_devices > 0:
                test_devices += 1
        return test_devices
