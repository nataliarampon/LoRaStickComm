#! /bin/bash
cat results/scenario2/64k/LTP-UDP-64k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2d/LTP-UDP-64k-512b.txt
cat results/scenario2/128k/LTP-UDP-128k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2d/LTP-UDP-128k-512b.txt
cat results/scenario2/256k/LTP-UDP-256k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2d/LTP-UDP-256k-512b.txt
cat results/scenario2/512k/LTP-UDP-512k-512b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2d/LTP-UDP-512k-512b.txt
cd ../experiments/scripts/graphics/files/figure2d/
gnuplot figure2d.plot
cp * ../../../../plots/figure2d/
cd ../../../../../ltp-proto/
