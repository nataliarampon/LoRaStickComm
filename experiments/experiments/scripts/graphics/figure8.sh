#! /bin/bash

# Figure 8 - UDP LTP 1kbps 128b payload size
cat results/scenario2/1k/LTP-UDP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure8/LTP-UDP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure8/
gnuplot figure8.plot
cd ../../../../../ltp-proto/
