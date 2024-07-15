# Automatic Telnet Password Changer

A Python script that scans all the computers on the host's netwotk for open Telnet ports.

If an open Telnet port has been detected, it will check if the password is weak by checking if it's identical to the passwords in the defaults.json file, and will change the password to a strong one if needed.

NOTE: The script has been verified to work on Debian 11 and Ubuntu 18.04.6 machines, while running on a Windows 10 machine.

## Prerequisites

Python 3.9

Nmap

## Usage 

First, install Python and Nmap on your desired machine

**For Windows:**

Simply download the [Python](https://www.python.org/downloads/) and [Nmap](https://nmap.org/download#windows) installers, and execute them.

**For Linux:**

Use the following commands:

```bash
sudo apt-get install python3.9
```

```bash
sudo apt-get install nmap
```

Than, simply run the script:

**For Windows:**

Open the Command Line as Administrator, and than enter the following commands:

```bash
cd SCRIPT_PATH
python3 -m main.py
```

OR

```bash
cd SCRIPT_PATH
python3 -m main.py
```

**For Linux:**

Enter the following command:

```bash
cd SCRIPT_PATH
sudo python3 -m main.py
```

OR

```bash
cd SCRIPT_PATH
sudo python3 -m main.py
```



