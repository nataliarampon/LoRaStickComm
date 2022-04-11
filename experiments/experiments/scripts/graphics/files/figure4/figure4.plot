#!gnuplot -persist
set encoding utf8                         #### codec texto
set terminal postscript eps color lw 5 "Helvetica" 26

set output "fig4.eps"

set grid
set multiplot
set object rectangle from 3000,27 to 4000,33 lw 1
set arrow from 4000,27 to 6500,10 front lt 3
set grid ytics
set key maxrows 3 ##font "Helvetica, 20"
set xlabel "Downloaded size (Kbytes)"      #### xlabel
set ylabel "Throughput (KB/s)"
set title "\n"
#set label 1 "Average speed for data transfer\n Link 256Kbps" at graph 0.5,1.225 center font "Helvetica, 30"
set xrange [0:16050]
set xtics format '%.0s' ##font "Helvetica, 20"
set yrange [0:45]
plot 'LTP-WGET-256k.txt' using 1:(32) title 'Nominal link speed' with lines lw 1,\
     'LTP-WGET-256k.txt' using 1:2 title "With LTP" with lines lw 1,\
     'STD-WGET-256k.txt' using 1:2 title "Without LTP"  with lines lw 1
unset grid
reset
set origin 0.48,0.25
set size 0.3,0.25
set bmargin 0; set tmargin 0; set lmargin 0; set rmargin 0
clear
unset key
set xrange [3000:4000]
set xtics (3000,4000) format '%.0s' ##font "Helvetica, 15"
set yrange [27:33]
set ytics (27,33) ##font "Helvetica, 15"
plot 'LTP-WGET-256k.txt' using 1:(32) with lines lw 1,\
     'LTP-WGET-256k.txt' using 1:2 with lines lw 1,\
     'STD-WGET-256k.txt' using 1:2 with lines lw 1
unset multiplot
