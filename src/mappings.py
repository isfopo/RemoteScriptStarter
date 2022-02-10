"""
  This file can be used to create constants for your MIDI mappings
  in order to be able to easily modify and change and MIDI notes or
  CCs that are used throughout your script.

  On the main branch this file will only contain basic, assumed mappings
  but other branches could contain more or less depending on what the
  script need. Feel free to change these on your scripts as well.

  Example:

  PLAY = 85
  STOP = 60
  REC = 86
  TAPTEMPO = 3

  As you can see, this is simply assigning number, that represent MIDI note
  or CCs, depending on how they are used in the context of the script.

  To add these an another file, add:

  from mappings import *

  with other import

  These mappings are then "loaded" into script by initialing an array of
  buttons and slider in the method `_load_mappings` which runs at __init__
  and will load this array into `self._note_map` and `self._ctrl_map` for
  Midi Notes and Midi CCs respectively.

  Any assignment to `-1` is ignored.
"""


class types:
    NOTE = 0
    CC = 1


BUTTONCHANNEL = 0
SLIDERCHANNEL = 1

PLAY = 56  # Global play
STOP = 57  # Global stop
REC = 58  # Global record
TAPTEMPO = 59  # Tap tempo
NUDGEUP = 60  # Tempo Nudge Up
NUDGEDOWN = 61  # Tempo Nudge Down
LOOP = 62  # Loop on/off
PUNCHIN = 63  # Punch in
PUNCHOUT = 64  # Punch out
OVERDUB = 65  # Overdub on/off
METRONOME = 66  # Metronome on/off
ARR_OVERDUB = 67

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE

TEMPOCONTROL = 48
SONGPOSITIONCONTROL = 49
