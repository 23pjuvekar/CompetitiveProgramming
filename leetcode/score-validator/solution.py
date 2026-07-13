class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:

        counter = 0
        score = 0
        for i in range(len(events)):
            if events[i] == "W":
                counter += 1
            elif events[i] == "WD" or events[i] == "NB": 
                score += 1
            else:
                score += int(events[i])
            if counter == 10:
                break
        
        return [score, counter]
