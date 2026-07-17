class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        number_of_teams = len(votes[0])
        position_counts = {team: [0] * number_of_teams for team in votes[0]}

        for vote in votes:
            for position, team in enumerate(vote):
                position_counts[team][position] += 1

        candidate_teams = list(position_counts.keys())
        candidate_teams.sort(key=lambda team: (position_counts[team], [-ord(character) for character in team]), reverse=True)

        return "".join(candidate_teams)
