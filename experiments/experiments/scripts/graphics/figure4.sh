#! /bin/bash

# Figure 4 - TCP Standard 1kbps 88b payload size
cat results/scenario1/1k/STD-TCP-1k-88b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure4/STD-TCP-1k-88b.txt
cd ../experiments/scripts/graphics/files/figure4/
gnuplot figure4.plot
cd ../../../../../ltp-proto/
