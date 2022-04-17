#! /bin/bash

# Figure 9 - UDP LTP 1kbps 200b payload size
cat results/scenario3/1k/LTP-UDP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure9/LTP-UDP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure9/
gnuplot figure9.plot
cp * ../../../../plots/figure9/
cd ../../../../../ltp-proto/
