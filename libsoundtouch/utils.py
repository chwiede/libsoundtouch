"""Utils for the Bose Soundtouch Device."""

from enum import Enum


class Key(Enum):
    """Keys of the device."""

    PLAY = 'PLAY'
    PAUSE = 'PAUSE'
    PLAY_PAUSE = 'PLAY_PAUSE'
    STOP = 'STOP'
    PREV_TRACK = 'PREV_TRACK'
    NEXT_TRACK = 'NEXT_TRACK'
    THUMBS_UP = 'THUMBS_UP'
    THUMBS_DOWN = 'THUMBS_DOWN'
    BOOKMARK = 'BOOKMARK'
    POWER = 'POWER'
    MUTE = 'MUTE'
    VOLUME_UP = 'VOLUME_UP'
    VOLUME_DOWN = 'VOLUME_DOWN'
    PRESET_1 = 'PRESET_1'
    PRESET_2 = 'PRESET_2'
    PRESET_3 = 'PRESET_3'
    PRESET_4 = 'PRESET_4'
    PRESET_5 = 'PRESET_5'
    PRESET_6 = 'PRESET_6'
    AUX_INPUT = 'AUX_INPUT'
    SHUFFLE_OFF = 'SHUFFLE_OFF'
    SHUFFLE_ON = 'SHUFFLE_ON'
    REPEAT_OFF = 'REPEAT_OFF'
    REPEAT_ONE = 'REPEAT_ON'
    REPEAT_ALL = 'REPEAT_ALL'
    ADD_FAVORITE = 'ADD_FAVORITE'
    REMOVE_FAVORITE = 'REMOVE_FAVORITE'


class Source(Enum):
    """Music sources supported by the device."""

    SLAVE_SOURCE = "SLAVE_SOURCE"
    INTERNET_RADIO = "INTERNET_RADIO"
    PANDORA = "PANDORA"
    AIRPLAY = "AIRPLAY"
    STORED_MUSIC = "STORED_MUSIC"
    AUX = "AUX"
    OFF_SOURCE = "OFF_SOURCE"
    CURRATED_RADIO = "CURRATED_RADIO"
    STANDBY = "STANDBY"
    UPDATE = "UPDATE"
    DEEZER = "DEEZER"
    SPOTIFY = "SPOTIFY"
    IHEART = "IHEART"
