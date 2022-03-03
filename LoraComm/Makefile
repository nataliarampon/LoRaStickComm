PORT=/dev/ttyUSB0

run:
	sudo python3 radio_duplex.py $(PORT)

interactive:
	sudo python3 radio_duplex.py $(PORT) --interactive

clean:
	rm -rf __pycache__
	killall socat