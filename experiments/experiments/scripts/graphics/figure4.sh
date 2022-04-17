#! /bin/bash

# Figure 4 - TCP Standard 1kbps 64b payload size
cat results/scenario1/1k/STD-TCP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure4/STD-TCP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure4/
gnuplot figure4.plot
cp * ../../../../plots/figure4/
cd ../../../../../ltp-proto/
