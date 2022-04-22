#! /bin/bash

# Figure 6 - TCP Standard 1kbps 200b payload size
cat results/scenario3/1k/STD-TCP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure6/STD-TCP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure6/
gnuplot figure6.plot
cd ../../../../../ltp-proto/
