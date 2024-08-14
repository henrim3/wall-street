import matplotlib.pyplot as plt

class dataCollector:
    def __init__(self, teams):
        self.data = {}  #{player: [ (round, captial)]}
        for team in teams:
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


