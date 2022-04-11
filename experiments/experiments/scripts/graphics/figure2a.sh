#! /bin/bash
cat results/scenario1/64k/LTP-TCP-64k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2a/LTP-TCP-64k-128b.txt
cat results/scenario1/128k/LTP-TCP-128k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2a/LTP-TCP-128k-128b.txt
cat results/scenario1/256k/LTP-TCP-256k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2a/LTP-TCP-256k-128b.txt
cat results/scenario1/512k/LTP-TCP-512k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2a/LTP-TCP-512k-128b.txt
cd ../experiments/scripts/graphics/files/figure2a/
gnuplot figure2a.plot
cp * ../../../../plots/figure2a/
cd ../../../../../ltp-proto/




