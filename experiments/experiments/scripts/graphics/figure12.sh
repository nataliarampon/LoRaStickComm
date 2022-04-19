#! /bin/bash

# Figure 12 - TCP LTP 1kbps 200b payload size
cat results/scenario12/1k/LTP-TCP-1k-200b.txt | grep sec | head -30 | tr - " " | awk '{print $4, $8}' > ../experiments/scripts/graphics/files/figure12/LTP-TCP-1k-200b.txt
cd ../experiments/scripts/graphics/files/figure12/
gnuplot figure12.plot
cd ../../../../../ltp-proto/
