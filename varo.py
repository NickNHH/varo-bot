import requests
import time

# File to store the log
log_file = "server_players_log.txt"


# Function to fetch players and return a set of their names
def fetch_players():
    url = "https://api.mcsrvstat.us/3/varo.swisshub.gg"
    print(f"Fetching players from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the response status code is 4XX or 5XX
        data = response.json()
        print(data["players"]["online"])
        if "players" in data and "list" in data["players"] and data["players"]["list"]:
            player_names = {player["name"] for player in data["players"]["list"]}
            print(f"Found {len(player_names)} players.")
            return player_names
        else:
            print("No players are currently online.")
            return set()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Keep track of the last set of players
last_players = set()

while True:
    current_players = fetch_players()
    if current_players is not None and current_players != last_players:
        # Update the last players set
        last_players = current_players

        # Log the change
        print("Players have changed. Updating log file.")

        # Write the new list of players to the log file with a timestamp
        with open(log_file, "a") as file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - Players online: {len(current_players)}\n")
            for name in sorted(current_players):
                file.write(f"  - {name}\n")
            file.write("\n")
    else:
        print("No change in players.")

    time.sleep(300)  # Wait for 5 minutes
