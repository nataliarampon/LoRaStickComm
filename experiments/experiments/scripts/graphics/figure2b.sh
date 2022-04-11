#! /bin/bash
cat results/scenario1/64k/LTP-UDP-64k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2b/LTP-UDP-64k-128b.txt
cat results/scenario1/128k/LTP-UDP-128k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2b/LTP-UDP-128k-128b.txt
cat results/scenario1/256k/LTP-UDP-256k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2b/LTP-UDP-256k-128b.txt
cat results/scenario1/512k/LTP-UDP-512k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2b/LTP-UDP-512k-128b.txt
cd ../experiments/scripts/graphics/files/figure2b/
gnuplot figure2b.plot
cp * ../../../../plots/figure2b/
cd ../../../../../ltp-proto/

