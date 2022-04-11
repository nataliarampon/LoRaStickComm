#! /bin/bash
cat results/scenario5/LTP-UDP-256k-1448b-h1-h4.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1b/LTP-UDP-256k-1448b-h1-h4.txt
cat results/scenario5/LTP-UDP-256k-1448b-h5-h8.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1b/LTP-UDP-256k-1448b-h5-h8.txt
cat results/scenario5/LTP-UDP-256k-1448b-h7-h2.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1b/LTP-UDP-256k-1448b-h7-h2.txt
cd ../experiments/scripts/graphics/files/figure1b/
gnuplot figure1b.plot
cp * ../../../../plots/figure1b/
cd ../../../../../ltp-proto/

