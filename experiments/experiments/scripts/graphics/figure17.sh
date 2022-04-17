#! /bin/bash

# Figure 17 - TCP Standard X LTP comparison 1kbps 128b payload size
cat results/scenario2/1k/STD-TCP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure17/STD-TCP-1k-128b.txt
cat results/scenario2/1k/LTP-TCP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure17/LTP-TCP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure17/
gnuplot figure17.plot
cp * ../../../../plots/figure17/
cd ../../../../../ltp-proto/
