#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

pg.display.init()
info = pg.display.Info()

SCREEN_W, SCREEN_H = info.current_w // 2, (info.current_h - 70) // 2
SCREEN_S = (SCREEN_W, SCREEN_H)

FRAMERATE = 60

NUMBER_OF_TILES_THAT_HORIZONTALLY_FITS_IN_SCREEN = 32
NUMBER_OF_TILES_THAT_VERTICALLY_FITS_IN_SCREEN = 16
TILES_IN_SCREEN_S = (
    NUMBER_OF_TILES_THAT_HORIZONTALLY_FITS_IN_SCREEN,
    NUMBER_OF_TILES_THAT_VERTICALLY_FITS_IN_SCREEN
)

TILE_W = SCREEN_W // NUMBER_OF_TILES_THAT_HORIZONTALLY_FITS_IN_SCREEN
TILE_H = TILE_W
TILE_S = (TILE_W, TILE_H)

SOUND_VOLUME = .1

CHUNK_W = 16
CHUNK_H = 64
CHUNK_S = (CHUNK_W, CHUNK_H)

CHUNK_IN_SCREEN = NUMBER_OF_TILES_THAT_HORIZONTALLY_FITS_IN_SCREEN // CHUNK_W