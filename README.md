# LoRaStickComm

## How to install (optional)
If you wish to use a virtual environment:
```
pip3 install --upgrade virtualenv
virtualenv venv
source venv/bin/activate 
```

And to leave the virtual environment:
```
deactivate
```

## How to install (required)
```
cd LoraComm
pip3 install -r requirements.txt
```
## How to run
To test the project using a virtual port (using `run_virtual_port_linux.sh` or `run_virtual_port_macos.sh`):
```
sudo su
brew install socat
./run_virtual_port_linux.sh
```

To run the project against an actual device connected to a port on your computer:
```
sudo su
make PORT=<port> run
```