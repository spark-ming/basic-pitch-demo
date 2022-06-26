import gradio as gr
from transcribe import Instrument, transcribe

demo = gr.Interface(
    title="Automatic Music Transcription",
    description="AMT based on Spotify's Basic Pitch.",
    allow_flagging="never",
    fn=transcribe,
    inputs=[
        gr.Audio(label="Original Audio", type="filepath"),
        gr.Dropdown(label="Instrument", choices=[i.value for i in Instrument]),
    ],
    outputs=[gr.Audio(label="Synthesized"), gr.File(label="MIDI File")],
)

demo.launch(server_name='0.0.0.0')
