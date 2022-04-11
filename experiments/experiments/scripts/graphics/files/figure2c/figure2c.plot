#!gnuplot -persist
set encoding utf8                         #### codec texto
set terminal postscript eps color lw 5 "Helvetica" 26


#set style data histogram                  #### histograma
#set style histogram errorbars #errorbars #rowstacked            #### pilha
#set boxwidth 0.75

set output "fig2c.eps"

#set datafile separator ","
#set xtics ('Plano' 0.17,'RSA' 1.17,'Papanis' 2.15,'Proposta' 3.20)

#set format y "%0.1t*10^{%S}"
#set format y "%.0s %c"


#set key outside horizontal top left
#set key invert reverse Left outside


set grid
set multiplot
#set object rectangle from 750,0.3 to 1200,3
#set arrow from 1000,3 to 750,5 front lt 3
set grid ytics
set key maxrows 2 ##font "Helvetica, 15"
set xlabel "Time (sec)"      #### xlabel
set ylabel "TCP Throughput (Kbps)"
set title "\n"
#set label 1 "Throughput Single link with 64k, 128k, 256k and\n 512k TCP packets of 512 bytes, with tag" at graph 0.5,1.225 center font "Helvetica, 30"
set xrange [0:900]
set yrange [0:600]
plot 'LTP-TCP-64k-512b.txt' using 1:2 title "64k" with lines lw 2,\
     'LTP-TCP-128k-512b.txt' using 1:2 title "128k" with lines lw 2,\
     'LTP-TCP-256k-512b.txt' using 1:2 title "256k" with lines lw 2,\
     'LTP-TCP-512k-512b.txt' using 1:2 title "512k" with lines lw 2

unset grid
#reset
#set origin 0.21,0.5
#set size 0.3,0.25
#set bmargin 0; set tmargin 0; set lmargin 0; set rmargin 0
#clear
#unset key
#set xrange [750:1200]
#set xtics (750,1200) font "Helvetica, 15"
#set yrange [0.3:3]
#set ytics (0.3,3) font "Helvetica, 15"
#plot 'new_LTP-UDP-512k-1u-1448b.txt' using 1:3 with linespoints lw 3,\
#     'new_STD-UDP-512k-1u-1448b.txt' using 1:3 with linespoints lw 3
unset multiplot
