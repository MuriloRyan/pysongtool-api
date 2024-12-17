from fastapi import FastAPI

from pysongtool.pysongtool import PySongTool

from pysongtool.data.scales import scales_list
from pysongtool.data.chords import chord_list

from pysongtool.exceptions.UnknownChord import UnknownChord
from pysongtool.exceptions.UnknownScale import WrongScale
from pysongtool.exceptions.WrongNote import WrongNote

import validations

app = FastAPI()
tool = PySongTool()

@app.get('/')
def index():
    return {'message': 'Hello, World!'}

@app.get('/get_scale/')
def get_scale(note: str, scale: str):
    validation = validations.get_scale_validation(note, scale, scales_list)

    if validation['is_valid'] == False:
        return validation

    return tool.scale(note, scale)

@app.get('/get_chord')
def get_chord(note: str, chord: str):
    validation = validations.get_chord_validation(note, chord, chord_list)

    if validation['is_valid'] == False:
        return validation
    
    return tool.chord(note, chord)

@app.get('/all_chords/')
def all_chords(note: str):
    validation = validations.note_validation(note)

    if validation['is_valid'] == False:
        return validation

    return tool.all_chords(note)