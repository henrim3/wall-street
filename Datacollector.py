import matplotlib.pyplot as plt

class dataCollector:
    def __init__(self, tteams):
        self.data = {}  #{player: [ (round, captial)]}
        self.teams = tteams
        for team in tteams:
            for player in team.players:
                self.data[player.name] = []
    def addData(self, player, data):
        self.data[player.name].append(data)
    
    def plotdata(self):
        plt.figure(figsize=(10, 6))
        
        for player, rounds_capital in self.data.items():
            # Separate rounds and capital values
            rounds = [round_ for round_, capital in rounds_capital]
            capital = [capital for round_, capital in rounds_capital]
            
            # Plot the player's capital per round
            plt.plot(rounds, capital, marker='o', label=player)
        
        # Adding titles and labels
        plt.title('Capital per Round for Each Player')
        plt.xlabel('Round')
        plt.ylabel('Capital')
        plt.legend()
        plt.grid(True)
        
        # Set x-axis ticks to integers only
        plt.xticks(range(min(rounds), max(rounds) + 1))

        # Show the plot
        plt.show()

    def plotteamdata(self, teamdata):
        plt.figure(figsize=(10, 6))
        
        for team in teamdata.keys():
            # Separate rounds and capital values
            rounds = range(len(teamdata[team]))
            capital = teamdata[team]
            
            # Plot the player's capital per round
            plt.plot(rounds, capital, marker='o', label=team)
        
        # Adding titles and labels
        plt.title('Capital per Round for Each Team')
        plt.xlabel('Round')
        plt.ylabel('Capital')
        plt.legend()
        plt.grid(True)
        
        # Set x-axis ticks to integers only
        plt.xticks(range(min(rounds), max(rounds) + 1))

        # Show the plot
        plt.show()

    def requestSummary(self):
        while True:
            raw_input: str = input("Would you like a summary of the player statistics? (Y or N): ")
            if raw_input == "Y":
                print()
                for player in self.data.keys():
                    print(f"\nPlayer {player}:")
                    for round in range(len(self.data[player])):
                        print(f"  Round {self.data[player][round][0]}: ${self.data[player][round][1]:,.2f}")
                    print(f"Total change: ${(self.data[player][-1][1] - self.data[player][0][1]):,.2f}")
                break
            elif raw_input != "N":
                print("\nError: Input must be Y or N\n")
            else:
                break
        print()
        while True:
            raw_input: str = input("Would you like a graph of the player statistics? (Y or N): ")
            if raw_input == "Y":
                self.plotdata()
                break
            elif raw_input != "N":
                print("\nError: Input must be Y or N\n")
            else:
                break
        print()
        while True:
            raw_input: str = input("Would you like a summary of the team statistics? (Y or N): ")
            if raw_input == "Y":
                teamdata = {}
                for team in self.teams:
                    teamdata[team.name] = [0] * len(self.data[team.players[0].name])
                    for player in team.players:
                        teamdata[team.name]
                        for round in range(len(self.data[player.name])):
                            teamdata[team.name][round] += self.data[player.name][round][1]
                    print(f"\nTeam {team.name}:")
                    for round in range(len(teamdata[team.name])):
                        print(f"  Round {round}: ${teamdata[team.name][round]:,.2f}")
                    print(f"Total change: ${(teamdata[team.name][-1] - teamdata[team.name][0]):,.2f}")
                break
            elif raw_input != "N":
                print("\nError: Input must be Y or N\n")
            else:
                break
        print()
        while True:
            raw_input: str = input("Would you like a graph of the team statistics? (Y or N): ")
            if raw_input == "Y":
                self.plotteamdata(teamdata)
                break
            elif raw_input != "N":
                print("\nError: Input must be Y or N\n")
            else:
                break
