#! /bin/bash

# Figure 11 - TCP LTP 1kbps 128b payload size
cat results/scenario2/1k/LTP-TCP-1k-128b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure11/LTP-TCP-1k-128b.txt
cd ../experiments/scripts/graphics/files/figure11/
gnuplot figure11.plot
cd ../../../../../ltp-proto/
