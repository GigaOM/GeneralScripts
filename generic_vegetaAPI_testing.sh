#!/bin/bash
#HTML output   just copy and past lines below the HTML and Text Ouput, and run as many tests as you like

echo "GET http://IP/HOSTNAME"  | vegeta attack -duration=1s -rate=1000 -output=results-http.bin && cat results-http.bin | ./vegeta plot --title="" > Results.html

#Text output
echo "GET http://IP/HOSTNAME"  | vegeta attack -duration=1s -rate=1000 | vegeta report --type=text

exit
