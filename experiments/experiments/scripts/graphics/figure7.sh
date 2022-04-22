#! /bin/bash

# Figure 7 - UDP LTP 1kbps 88b payload size
cat results/scenario1/1k/LTP-UDP-1k-88b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure7/LTP-UDP-1k-88b.txt
cd ../experiments/scripts/graphics/files/figure7/
gnuplot figure7.plot
cd ../../../../../ltp-proto/
