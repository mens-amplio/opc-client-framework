from model import Model
from renderer import Renderer
from controller import AnimationController
from effectlayer import *
from playlist import Playlist
from threads import PlaylistAdvanceThread
from random import random

if __name__ == '__main__':

    # in a real implementation the model would require additional data to initialize, but
    # here we just need to know the number of LEDs
    model = Model(40)

    # a playlist. each entry in a playlist can contain one or more effect layers
    # (if more than one, they are all rendered into the same frame...mixing method 
    # is determined by individual effect layers' render implementations)
    playlist = Playlist([
        [
            SnowstormLayer(),
            ColorBlinkyLayer(),
        ],
        [
            SnowstormLayer(),
        ],
    ])

    # master parameters, used in rendering and updated by playlist advancer thread
    masterParams = EffectParameters()

    # the renderer manages a playlist (or dict of multiple playlists), as well as transitions
    # and gamma correction
    renderer = Renderer(playlists={'all': playlist}, gamma=2.2)

    # the controller manages the animation loop - creates frames, calls into the renderer
    # at appropriate intervals, updates the time stored in master params, and sends frames
    # out over OPC
    controller = AnimationController(model, renderer, masterParams)

    # a thread that periodically advances the active playlist within the renderer.
    # TODO: example to demonstrate swapping between multiple playlists with custom fades
    advancer = PlaylistAdvanceThread(renderer, switchInterval=10)
    advancer.start()

    # go!
    controller.drawingLoop()