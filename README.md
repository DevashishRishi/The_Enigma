# Enigma Simulator

## Description
This project is a simulation of the **Enigma machine**, a cipher device used during World War II for encrypting and decrypting messages. The simulator is built using **Python** and **Pygame**, providing an interactive graphical interface to visualize how the Enigma machine processes input characters.

## Features
- Fully functional **Enigma machine** simulation
- Interactive **graphical representation** of signal paths
- Configurable **rotors, reflector, plugboard** settings
- Real-time visualization of letter encoding and decoding
- Implemented using **Pygame** for a smooth UI experience

## Installation
### Prerequisites
Ensure you have **Python 3.10+** installed. If not, download it from [Python's official site](https://www.python.org/downloads/).

### Clone the Repository
```sh
git clone https://github.com/yourusername/enigma-simulator.git
cd enigma-simulator
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
Run the main script to start the Enigma simulator:
```sh
python main.py
```

### Controls
- Type a letter to see its encrypted output.
- Observe the signal path as it travels through the **plugboard, rotors, and reflector**.
- Adjust rotor settings for custom encryption.
- Press **Esc** to exit the simulation.

## Project Structure
```
├── enigma  # Core logic of the Enigma machine
│   ├── rotor.py      # Implementation of rotors
│   ├── reflector.py  # Reflector logic
│   ├── plugboard.py  # Plugboard connections
├── draw.py   # Handles graphical rendering
├── main.py   # Entry point for running the simulator
├── assets/   # Image and font resources
├── README.md # Project documentation
```

## Known Issues
- Pygame may **block three-finger gestures** on some Windows touchpads.
- Running in **fullscreen mode** might interfere with system hotkeys.

## Contributing
Feel free to submit **issues, feature requests, or pull requests**!

## License
This project is licensed under the **MIT License**.

