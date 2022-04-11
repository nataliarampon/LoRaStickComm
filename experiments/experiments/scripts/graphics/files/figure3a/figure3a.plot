#!gnuplot -persist
set encoding utf8                         #### codec texto
set terminal postscript eps color lw 5 "Helvetica" 26

set output "fig3a.eps"

set grid
set multiplot
set object rectangle from 600,170 to 800,240
set arrow from 600,170 to 490,160 front lt 3
set grid ytics
set key maxrows 1 ##font "Helvetica, 20"
set xlabel "Time (sec)"      #### xlabel
set ylabel "UDP Throughput (Kbps)"
set title "\n"
#set label 1 "Throughput UDP Link 256Kbps\n Payload 128 Bytes" at graph 0.5,1.225 center font "Helvetica, 30"
set xrange [0:900]
set yrange [0:300]
plot 'LTP-UDP-256k-128b.txt' using 1:2 title "With LTP" with lines lw 2,\
     'STD-UDP-256k-128b.txt' using 1:2 title "Without LTP"  with lines lw 2

unset grid
reset
set origin 0.28,0.25
set size 0.3,0.25
set bmargin 0; set tmargin 0; set lmargin 0; set rmargin 0
clear
unset key
set xrange [600:800]
set xtics (600,800) ##font "Helvetica, 15"
set yrange [170:240]
set ytics (170,240) ##font "Helvetica, 15"
set arrow from 610,220 to 610,190 heads front lt 3
set label "23.5% avg. gain" at 620,205
plot 'LTP-UDP-256k-128b.txt' using 1:2 with lines lw 2,\
     'STD-UDP-256k-128b.txt' using 1:2 with lines lw 2
unset multiplot
