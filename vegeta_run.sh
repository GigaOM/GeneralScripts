#!/bin/bash

echo "GET http://216.202.250.204/" | ./vegeta attack -duration=1s -rate=1000 -output=Lumen-Edge-results-http-get.bin && cat Lumen-Edge-results-http-get.bin | ./vegeta plot --title="Lumen Edg Latency Results " > LumanEdge-Results.html

echo "GET http://fromthemindofnobody.com/" | ./vegeta attack -duration=1s -rate=1000 -output=Luman-VMWare-Instance-results-http.bin && cat Luman-VMWare-Instance-results-http.bin | ./vegeta plot --title="Luman Private Cloud Results" > LumanPC-Results.html

echo "GET http://54.176.133.113/" | ./vegeta attack -duration=1s -rate=1000 -output=AWS-Edge-results-http-get.bin && cat AWS-Edge-results-http-get.bin | ./vegeta plot --title="AWS Edge Results" > AWSEdge-Results.html

echo "GET http://wrightsinfosec.com/" | ./vegeta attack -duration=1s -rate=1000 -output=AWS-EC2-results-http.bin && cat AWS-Instance-results-http.bin | ./vegeta plot --title="AWS Private Cloud" > AWSPC-Results.html

exit
