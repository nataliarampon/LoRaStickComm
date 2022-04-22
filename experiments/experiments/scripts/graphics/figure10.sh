#! /bin/bash

# Figure 10 - TCP LTP 1kbps 88b payload size
cat results/scenario1/1k/LTP-TCP-1k-88b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure10/LTP-TCP-1k-88b.txt
cd ../experiments/scripts/graphics/files/figure10/
gnuplot figure10.plot
cd ../../../../../ltp-proto/
