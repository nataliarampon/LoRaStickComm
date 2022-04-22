#! /bin/bash

# Figure 15 - UDP Standard X LTP comparison 1kbps 200b payload size
cat results/scenario3/1k/STD-UDP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure15/STD-UDP-1k-200b.txt
cat results/scenario3/1k/LTP-UDP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure15/LTP-UDP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure15/
gnuplot figure15.plot
cd ../../../../../ltp-proto/
