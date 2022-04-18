#!gnuplot -persist
set encoding utf8
set terminal postscript eps color lw 5 "Helvetica" 26


#set style data histogram                 
#set style histogram errorbars #errorbars #rowstacked
#set boxwidth 0.75

set output "fig1.eps"

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
set key maxrows 3 ## font "Helvetica, 15"
set xlabel "Time (sec)"      #### xlabel
set ylabel "UDP Throughput (Kbps)"
set title "\n"
#set label 1 "Throughput UDP Link 1Kbps\n Payload 64 Bytes" at graph 0.5,1.225 center font "Helvetica, 30"
set xrange [0:900]
set yrange [0:500]
plot 'STD-UDP-1k-64b.txt' using 1:2 with lines lc rgb "orange" lw 2

unset grid
unset multiplot