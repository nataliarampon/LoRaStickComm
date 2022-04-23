#! /bin/bash

# Figure 19 -  Aggregate of three payload sizes (88b, 128b, 200b) for Standard UDP 1kbps
cat results/scenario1/1k/STD-UDP-1k-88b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure19/STD-UDP-1k-88b.txt
cat results/scenario2/1k/STD-UDP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure19/STD-UDP-1k-128b.txt
cat results/scenario3/1k/STD-UDP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure19/STD-UDP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure19/
gnuplot figure19.plot
cp fig19.eps ../../../../plots/
cd ../../../../../ltp-proto/
