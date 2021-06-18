# reimagined-system
![demo](https://github.com/shefa/reimagined-system/raw/main/demo.gif)
Want to send MIDI signals from your phone to Reaper running on your PC?
This script allows you to use your phone (or any device actually) as a wireless midi controller - 
You can play MIDI instruments from your phone, or use MIDI signals to trigger DAW actions.

# What
Using Flask, this minimalistic script sets up a web API on your PC, which uses `rtmidi` python module to send some midi events to a virtual MIDI device. This virtual MIDI device can then be picked up by Reaper or any DAW.

The script also sets up a simple web page with a few buttons. When clicked, the user sends an AJAX request to the API endpoint.

# Usage
1. Install and run [loopMIDI](http://www.tobias-erichsen.de/software/loopmidi.html)
2. Add a new virtual port (name doesn't matter)
3. Configure DAW to accept the virtual midi as input. ![MIDI config](https://github.com/shefa/reimagined-system/raw/main/daw_midi.png)
4. `cd reimagined-system && flask run --host=0.0.0.0`
6. Open the webpage on phone, click stuff and you will receive MIDI in reaper!