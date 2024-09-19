import sys
import codingame
from collections import defaultdict
from tabulate import tabulate

def main(handles):
    client = codingame.Client()
    player_stats = defaultdict(lambda: {'count': 0, 'sum': 0})

    # Iterate over each handle provided
    for handle in handles:
        try:
            # Get the Clash of Code using the public handle
            coc = client.get_clash_of_code(handle)
            players = coc.players

            # Loop through each player to gather ranking information
            for player in players:
                if player.score is not None:  # Check if the player has a ranking
                    player_stats[player.pseudo]['count'] += 1
                    player_stats[player.pseudo]['sum'] += player.rank
        except Exception as e:
            print(f"Error retrieving clash {handle}: {e}")

    # Sort players by participation count (descending) and then by ranking sum (ascending)
    sorted_players = sorted(player_stats.items(), key=lambda x: (-x[1]['count'], x[1]['sum']))

    # Prepare data for tabulation
    table_data = [[player_name, data['count'], data['sum']] for player_name, data in sorted_players]
    
    # Print the results in a formatted table
    print(tabulate(table_data, headers=['Player Name', 'Number of Finished Clashes', 'Ranking Sum'], tablefmt='grid'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clashofcode-agregator.py <handle1> <handle2> ...")
    else:
        main(sys.argv[1:])
