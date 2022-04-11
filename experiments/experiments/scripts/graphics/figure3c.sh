#! /bin/bash
cat results/scenario3/256k/LTP-UDP-256k-1024b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3c/LTP-UDP-256k-1024b.txt
cat results/scenario3/256k/STD-UDP-256k-1024b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3c/STD-UDP-256k-1024b.txt
cd ../experiments/scripts/graphics/files/figure3c/
gnuplot figure3c.plot
cp * ../../../../plots/figure3c/
cd ../../../../../ltp-proto/


