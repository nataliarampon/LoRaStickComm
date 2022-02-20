# LoRaStickComm

An interface permitting a half-duplex communication between two LoStik devices.

This project was created having Unix operating systems in mind.

---
<br/>

## How to install
<details>
  <summary>Install instructions</summary>

  ### (Optional) Create a virtual environment
  If you wish to use a virtual environment, follow the below steps to create one:

  ```
  pip3 install --upgrade virtualenv
  virtualenv venv 
  ```

  To enter the virtual environment:

  ```
  source venv/bin/activate
  ```

  And to leave the virtual environment:
  ```
  deactivate
  ```

  ### Install the requirements
  This project requires Python 3, preferably version 3.7 or later. Install the project requirements and dependencies by executing:
  ```
  cd LoraComm
  pip3 install -r requirements.txt
  ```
</details>

---
<br/>

## How to run
<details>
  <summary>Running instructions</summary>
  To test the project using a virtual port (using `run_virtual_port_linux.sh` or `run_virtual_port_macos.sh`):

  ```
  sudo su
  brew install socat
  ./run_virtual_port_linux.sh
  ```

  To run the project against an actual LoStik device connected to a port on your computer:

  ```
  sudo su
  make PORT=<port> run
  ```
</details>

---
<br/>

## Code Architecture
The LoStik device used USB 2.0 connectivity, according to [their documentation](https://ronoth.com/products/lostik). Since [USB 2.0 specification](https://www.usb.org/document-library/usb-20-specification) defines it to use a half-duplex communication, one cannot achive a full-duplex communication using LoStik devices, as the USB 2.0 connector does not support it.

Thus, this interface is written having half-duplex communication in mind. There are then two threads running to form the interface, one dedicated to reading messages which arrive through the device and another meant to write messages to be transmitted by the device once they are available.