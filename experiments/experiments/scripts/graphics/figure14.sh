#! /bin/bash

# Figure 14 - UDP Standard X LTP comparison 1kbps 128b payload size
cat results/scenario2/1k/STD-UDP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure14/STD-UDP-1k-128b.txt
cat results/scenario2/1k/LTP-UDP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure14/LTP-UDP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure14/
gnuplot figure14.plot
cd ../../../../../ltp-proto/
