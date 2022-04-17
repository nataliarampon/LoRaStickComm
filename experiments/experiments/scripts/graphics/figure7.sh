#! /bin/bash

# Figure 7 - UDP LTP 1kbps 64b payload size
cat results/scenario1/1k/LTP-UDP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure7/LTP-UDP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure7/
gnuplot figure7.plot
cp * ../../../../plots/figure7/
cd ../../../../../ltp-proto/
