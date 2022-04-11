#! /bin/bash
cat results/scenario2/256k/LTP-UDP-256k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3b/LTP-UDP-256k-512b.txt
cat results/scenario2/256k/STD-UDP-256k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3b/STD-UDP-256k-512b.txt
cd ../experiments/scripts/graphics/files/figure3b/
gnuplot figure3b.plot
cp * ../../../../plots/figure3b/
cd ../../../../../ltp-proto/


