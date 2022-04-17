#! /bin/bash

# Figure 2 - UDP Standard 1kbps 128b payload size
cat results/scenario2/1k/STD-UDP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure2/STD-UDP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure2/
gnuplot figure2.plot
cp * ../../../../plots/figure2/
cd ../../../../../ltp-proto/
