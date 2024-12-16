from fastapi import FastAPI

from pysongtool.pysongtool import PySongTool

from pysongtool.data.scales import scales_list

from pysongtool.exceptions.UnknownChord import UnknownChord
from pysongtool.exceptions.UnknownScale import WrongScale
from pysongtool.exceptions.WrongNote import WrongNote

import validations
import validations.get_scale

app = FastAPI()
tool = PySongTool()

@app.get('/')
def index():
    return {
        'message': 'Hello, take a look at /docs and try all api endpoints!'
    }

@app.get('/get_scale/')
def get_scale(note: str, scale: str):
    validation = validations.get_scale_validation(note, scale, scales_list)

    if validation['is_valid'] == False:
        return validation

    return tool.scale(note, scale)