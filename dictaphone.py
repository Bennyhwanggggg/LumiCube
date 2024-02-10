"""
The top button starts the recording, the middle stops it and the bottom plays what you've recorded.
"""

file = "voicenote.mp3"
while True:
    # Wait up to 100 seconds for the next action
    action = buttons.get_next_action(100.0)
    if action == "top":
        microphone.start_recording(file)
    elif action == "middle":
        microphone.stop_recording()
    elif action == "bottom":
        speaker.play(file)
