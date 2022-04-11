#! /bin/bash

echo 'Copying topology'
cp ../experiments/scripts/topologies/topology64std.json ./topology.json

echo 'Copying run_exercise'
cp ../experiments/scripts/run_exercise/run_exercise64std.py ../utils/run_exercise.py

echo 'Coping standard proto and controllers'
cp ../standard/basic_tunnel.p4 ./ltp-proto.p4
cp ../standard/s1-runtime.json ./s1-runtime.json
cp ../standard/s2-runtime.json ./s2-runtime.json
cp ../standard/s3-runtime.json ./s3-runtime.json

echo 'Copying topologies to scenario results'
cp topology.json results/scenario1/64k/STD/
cp topology.json results/scenario2/64k/STD/
cp topology.json results/scenario3/64k/STD/
cp topology.json results/scenario4/64k/STD/

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
cp ../experiments/scripts/backup/s3controller.py ./s3controller.py

echo 'Removing standard controllers'
rm s1-runtime.json
rm s2-runtime.json
rm s3-runtime.json
