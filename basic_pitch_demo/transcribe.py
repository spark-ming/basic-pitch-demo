from enum import Enum

import tensorflow as tf
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH

basic_pitch_model = tf.saved_model.load(str(ICASSP_2022_MODEL_PATH))
sample_rate = 44100


class Instrument(Enum):
    PIANO = "Piano"
    EIGHTBIT = "8-bit"
    NOKIA = "Nokia"
    MEOW = "Meow"


def get_sound_font(instrument: Instrument):
    if instrument == Instrument.PIANO:
        return "./sound_fonts/piano.sf2"
    if instrument == Instrument.EIGHTBIT:
        return "./sound_fonts/8bit.sf2"
    if instrument == Instrument.NOKIA:
        return "./sound_fonts/nokia_3220.sf2"
    if instrument == Instrument.MEOW:
        return "./sound_fonts/meow.sf2"

    return None


def transcribe(audio: str, instrument: Instrument):
    model_output, midi_data, note_activations = predict(
        audio,
        basic_pitch_model,
    )

    export_file = audio + ".mid"

    midi_data.write(export_file)

    for i in midi_data.instruments:
        # For fluidsynth to work
        i.program = 0

    synth = midi_data.fluidsynth(sample_rate, sf2_path=get_sound_font(Instrument(instrument)))

    return [(sample_rate, synth.astype("float32")), export_file]
