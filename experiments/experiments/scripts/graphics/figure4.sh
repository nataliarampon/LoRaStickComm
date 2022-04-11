#! /bin/bash
cat results/scenario7/LTP-WGET-256k.txt | grep % | cut -d 'K' -f 1,2| tr K ' '| cut -c -6,63-67 > ../experiments/scripts/graphics/files/figure4/LTP-WGET-256k.txt
cat results/scenario7/STD-WGET-256k.txt | grep % | cut -d 'K' -f 1,2| tr K ' '| cut -c -6,63-67 > ../experiments/scripts/graphics/files/figure4/STD-WGET-256k.txt
cd ../experiments/scripts/graphics/files/figure4/
gnuplot figure4.plot
cp * ../../../../plots/figure4/
cd ../../../../../ltp-proto/

