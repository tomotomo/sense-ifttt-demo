# Requirements

Hardware

* Raspberry Pi (Zero / 3A+ / 3B / 3B+ / 4)
* SenseHAT
* Nature Remo

Softoware

* Raspberry Pi OS Buster
* Python3

## Setup Raspberry Pi

Enable SenseHAT

```bash
sudo apt update
sudo apt install sense-hat
sudo reboot
```

Download sample

```bash
git clone https://github.com/tomotomo/sense-ifttt-demo.git
cd sense-ifttt-demo
```

If you don't have a SenseHAT, use SenseHAT Emulator. (Maybe you need Raspberry Pi Desktop...)

Read [Sense-Emu Documentation](https://sense-emu.readthedocs.io/en/v1.0/install.html).

```bash
sudo apt-get update
sudo apt-get install python-sense-emu python3-sense-emu sense-emu-tools
```

## Run Demo

### 1.SenseHAT

```bash
python3 sense.py
```

### 2.IFTTT with SenseHAT

#### Create IFTTT Apps

Create Apps [here](https://ifttt.com/create)

IF|Event Name|THEN|select
---|---|---|---
Webooks|turn_on|Nature Remo|Turn on air conditioner
Webooks|turn_off|Nature Remo|Turn off air conditioner

#### Edit IFTTT Key

Get your IFTTT webhook key from [here](https://ifttt.com/maker_webhooks/settings) and edit `sense-ifttt.py`

```python
IFTTT_KEY = ''  # @param {type:"string"}
```

#### Run app

```bash
python3 sense-ifttt.py
```
