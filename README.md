# D2R-Autobuff
Simple Python script for automating a series of keypresses in the game Diablo II: Resurrected.

# Clone the repository
git clone https://github.com/username/diablo-key-sequence-automation.git

# Navigate to the project directory
> cd D2R-Autobuff

# Install the required Python packages
> pip install -r requirements.txt

You'll find a list of keys and a cooldown time:

> keys = ['f1', 'f1', 'f2', 'f2', 'w', 'f7', 'f7', 'f8', 'f8', 'w']

> cooldown_time = 120  # 2 minutes

The `keys` list should correspond to the hotkeys that you've set for your skills in the game. 
You can modify this list to match your particular setup. `w` should be your weapon swap key to switch to CTA and then back to primary.

The `cooldown_time` is the time in seconds that the script waits between executing the key sequences. 
It should be set to the cooldown time of the skill with the shortest cooldown.

# Run the script
> python autobuff.py

# Hotkeys
- 'u': Start or pause the key sequence
- 'r': Restart the key sequence
