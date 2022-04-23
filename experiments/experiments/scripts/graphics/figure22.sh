#! /bin/bash

# Figure 22 -  Aggregate of three payload sizes (88b, 128b, 200b) for LTP TCP 1kbps
cat results/scenario1/1k/LTP-TCP-1k-88b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure22/LTP-TCP-1k-88b.txt
cat results/scenario2/1k/LTP-TCP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure22/LTP-TCP-1k-128b.txt
cat results/scenario3/1k/LTP-TCP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure22/LTP-TCP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure22/
gnuplot figure22.plot
cp fig22.eps ../../../../plots/
cd ../../../../../ltp-proto/
