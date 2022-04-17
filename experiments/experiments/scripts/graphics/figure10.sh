#! /bin/bash

# Figure 10 - TCP LTP 1kbps 64b payload size
cat results/scenario1/1k/LTP-TCP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure10/LTP-TCP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure10/
gnuplot figure10.plot
cp * ../../../../plots/figure10/
cd ../../../../../ltp-proto/
