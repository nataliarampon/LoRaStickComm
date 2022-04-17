#! /bin/bash

# Figure 5 - TCP Standard 1kbps 128b payload size
cat results/scenario2/1k/STD-TCP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure5/STD-TCP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure5/
gnuplot figure5.plot
cp * ../../../../plots/figure5/
cd ../../../../../ltp-proto/
