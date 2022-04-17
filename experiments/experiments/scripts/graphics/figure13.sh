#! /bin/bash

# Figure 13 - UDP Standard X LTP comparison 1kbps 64b payload size
cat results/scenario1/1k/STD-UDP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure13/STD-UDP-1k-64b.txt
cat results/scenario1/1k/LTP-UDP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure13/LTP-UDP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure13/
gnuplot figure13.plot
cp * ../../../../plots/figure13/
cd ../../../../../ltp-proto/
