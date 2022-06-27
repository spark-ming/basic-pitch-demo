import gradio as gr
from transcribe import Instrument, transcribe

title = "Automatic Music Transcription"
description = "AMT based on Spotify's Basic Pitch."

outputs = [gr.Audio(label="Synthesized"), gr.File(label="MIDI File")]
instrument_dropdown = gr.Dropdown(
    label="Instrument", choices=[i.value for i in Instrument]
)

file_demo = gr.Interface(
    title=title,
    description=description,
    allow_flagging="never",
    fn=transcribe,
    examples=[["./notebooks/demo_data/nokia.mp3", "8-bit"]],
    inputs=[gr.Audio(label="Original Audio", type="filepath"), instrument_dropdown,],
    outputs=outputs,
)

recording_demo = gr.Interface(
    title=title,
    description=description,
    allow_flagging="never",
    fn=transcribe,
    inputs=[
        gr.Audio(label="Recording", source="microphone", type="filepath"),
        instrument_dropdown,
    ],
    outputs=outputs,
)

tabs = gr.TabbedInterface([file_demo, recording_demo], ["File Input", "Mic Input"],)

tabs.launch(server_name="0.0.0.0",)
