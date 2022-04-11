#! /bin/bash
cat results/scenario4/256k/LTP-UDP-256k-1448b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3d/LTP-UDP-256k-1448b.txt
cat results/scenario4/256k/STD-UDP-256k-1448b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3d/STD-UDP-256k-1448b.txt
cd ../experiments/scripts/graphics/files/figure3d/
gnuplot figure3d.plot
cp * ../../../../plots/figure3d/
cd ../../../../../ltp-proto/

