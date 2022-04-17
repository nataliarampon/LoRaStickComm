#! /bin/bash

# Figure 18 - TCP Standard X LTP comparison 1kbps 200b payload size
cat results/scenario3/1k/STD-TCP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure18/STD-TCP-1k-200b.txt
cat results/scenario3/1k/LTP-TCP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure18/LTP-TCP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure18/
gnuplot figure18.plot
cp * ../../../../plots/figure18/
cd ../../../../../ltp-proto/
