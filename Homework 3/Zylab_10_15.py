# Carolina Reyes
# 1563200

# Complete the Team class implementation. For the class method get_win_percentage(), the formula is:
# team_wins / (team_wins + team_losses)
# You can start with the following class definition:
# class Team: def init(self): self.teamname = 'none' self.teamwins = 0 self.team_losses = 0


# creates a class
class Team:
    # creates a constructor
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        percentage = self.team_wins / (self.team_wins + self.team_losses)  # calculates the percentage
        return percentage  # Calculates the percentage


if __name__ == '__main__':
    # calls the class
    team_1 = Team()
    # allows the user to input information
    team_1.team_name = input()
    team_1.team_wins = int(input())
    team_1.team_losses = int(input())

    # prints whether the team has a winning a average or a losing average
    if team_1.get_win_percentage() >= .50:
        print('Congratulations, Team {} has a winning average!'.format(team_1.team_name))
    else:
        print('Team {} has a losing average.'.format(team_1.team_name))
