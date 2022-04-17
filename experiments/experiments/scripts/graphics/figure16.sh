#! /bin/bash

# Figure 16 - TCP Standard X LTP comparison 1kbps 64b payload size
cat results/scenario1/1k/STD-TCP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure16/STD-TCP-1k-64b.txt
cat results/scenario1/1k/LTP-TCP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure16/LTP-TCP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure16/
gnuplot figure16.plot
cp * ../../../../plots/figure16/
cd ../../../../../ltp-proto/
