#! /bin/bash

# Figure 1 - UDP Standard 1kbps 64b payload size
cat results/scenario1/1k/STD-UDP-1k-64b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure1/STD-UDP-1k-64b.txt
cd ../experiments/scripts/graphics/files/figure1/
gnuplot figure1.plot
cp * ../../../../plots/figure1/
cd ../../../../../ltp-proto/
