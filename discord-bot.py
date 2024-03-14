import discord
import asyncio
import requests
import time
import os

# Your bot's token
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Channel ID where you want to send the message
CHANNEL_ID = 1217642237647785994

# Define the intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

async def log_players():
    await client.wait_until_ready()  # Wait until the client is ready
    channel = client.get_channel(CHANNEL_ID)
    last_players = set()

    while not client.is_closed():
        current_players = fetch_players()
        if current_players is not None and current_players != last_players:
            # Update the last players set
            last_players = current_players
            # Create the message to send
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f"{timestamp} - Players online: {len(current_players)}\n"
            message += "\n".join(sorted(current_players))
            # Send the message to the Discord channel
            if channel:  # Check if the channel was found
                await channel.send(message)
            else:
                print(f"Channel with ID {CHANNEL_ID} not found.")
        await asyncio.sleep(60)  # Wait for 10 minutes

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

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(log_players())

client.run(TOKEN)
