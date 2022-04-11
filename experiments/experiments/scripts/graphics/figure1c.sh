#! /bin/bash
cat results/scenario6/LTP-TCP-256k-1448b-h1-h6.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1c/LTP-TCP-256k-1448b-h1-h6.txt
cat results/scenario6/LTP-TCP-256k-1448b-h2-h7.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1c/LTP-TCP-256k-1448b-h2-h7.txt
cat results/scenario6/LTP-TCP-256k-1448b-h3-h8.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1c/LTP-TCP-256k-1448b-h3-h8.txt
cat results/scenario6/LTP-TCP-256k-1448b-h4-h9.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1c/LTP-TCP-256k-1448b-h4-h9.txt
cat results/scenario6/LTP-TCP-256k-1448b-h5-h10.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1c/LTP-TCP-256k-1448b-h5-h10.txt
cd ../experiments/scripts/graphics/files/figure1c/
gnuplot figure1c.plot
cp * ../../../../plots/figure1c/
cd ../../../../../ltp-proto/
