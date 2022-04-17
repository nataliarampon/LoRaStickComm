#! /bin/bash

# Figure 3 - UDP Standard 1kbps 200b payload size
cat results/scenario3/1k/STD-UDP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure3/STD-UDP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure3/
gnuplot figure3.plot
cp * ../../../../plots/figure3/
cd ../../../../../ltp-proto/
