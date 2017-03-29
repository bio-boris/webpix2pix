#!/usr/bin/env python

import os
from PIL import Image


def getFrames(gif_filepath):
    frame = Image.open(gif_filepath)
    nframes = 0
    while frame:
        try:
            frame.seek( nframes )
            yield frame
            nframes += 1
        except EOFError:
            break;
            
