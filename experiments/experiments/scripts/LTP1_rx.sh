#! /bin/bash

echo 'Copying topology'
cp ../experiments/scripts/topologies/topology1_rx.json ./topology.json

echo 'Copying run_exercise'
cp ../experiments/scripts/run_exercise/run_exercise1_rx.py ../utils/run_exercise.py

echo 'Copying ltp-proto'
cp ../experiments/scripts/backup/ltp-proto.p4 ./ltp-proto.p4

echo 'Copying controllers'
cp ../experiments/scripts/backup/s1controller.py ./s1controller.py
cp ../experiments/scripts/backup/s2controller.py ./s2controller.py

echo 'Copying switch runtimes'
cp ../standard/s2-runtime.json ./s2-runtime.json

echo 'Copying topologies to scenario results'
cp topology.json results/scenario1/1k/LTP/
cp topology.json results/scenario2/1k/LTP/
cp topology.json results/scenario3/1k/LTP/

echo 'Starting topology'
./run-me.sh

echo 'Restoring topology'
cp ../experiments/scripts/backup/topology.json ./topology.json

echo 'Restoring run_exercise'
cp ../experiments/scripts/backup/run_exercise.py ../utils/run_exercise.py

echo 'Restoring ltp-proto'
cp ../experiments/scripts/backup/ltp-proto.p4 ./ltp-proto.p4

echo 'Restoring controllers'
cp ../experiments/scripts/backup/s1controller.py ./s1controller.py
cp ../experiments/scripts/backup/s2controller.py ./s2controller.py