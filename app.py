from flask import Flask, render_template, Response, request, redirect, url_for
import rtmidi
import time

app = Flask(__name__)
midi_out = rtmidi.MidiOut()

@app.route("/")
def index():
    return render_template('index.html');

@app.route('/midi/<note>')
def midi(note=0):
    midi_out.open_port(1)
    with midi_out:
        midi_out.send_message([0x9C, int(note), 100])  # send NOTE_ON event on channel 13
        time.sleep(0.5)
        midi_out.send_message([0x8C, int(note), 0])
    midi_out.close_port()
    return note
    