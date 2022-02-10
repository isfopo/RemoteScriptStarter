from __future__ import with_statement

import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.TransportComponent import TransportComponent

from .mappings import *


class RemoteScriptStarter(ControlSurface):
    __module__ = __name__
    __doc__ = "Simple Starter Script"

    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

            self._note_map = []
            self._ctrl_map = []
            self._load_mappings()

            self._setup_transport()

            # write your init code here

    def disconnect(self):
        """clean up on disconnect"""
        ControlSurface.disconnect(self)
        return None

    def _setup_transport(self):
        transport = TransportComponent()
        transport.name = 'Transport'
        transport.set_play_button(self._note_map[PLAY])
        transport.set_stop_button(self._note_map[STOP])
        transport.set_record_button(self._note_map[REC])
        transport.set_nudge_buttons(
            self._note_map[NUDGEUP], self._note_map[NUDGEDOWN])
        transport.set_overdub_button(self._note_map[OVERDUB])
        transport.set_metronome_button(self._note_map[METRONOME])
        transport.set_tap_tempo_button(self._note_map[TAPTEMPO])
        transport.set_tempo_control(self._ctrl_map[TEMPOCONTROL])
        transport.set_loop_button(self._note_map[LOOP])
        transport.set_punch_buttons(
            self._note_map[PUNCHIN], self._note_map[PUNCHOUT])
        transport.set_arrangement_overdub_button(self._note_map[ARR_OVERDUB])

    def _load_mappings(self):
        momentary = True

        for note in range(128):
            button = ButtonElement(momentary, types.NOTE, BUTTONCHANNEL, note)
            button.name = 'Note_' + str(note)
            self._note_map.append(button)
        self._note_map.append(None)

        for ctrl in range(128):
            control = ButtonElement(momentary, types.CC, BUTTONCHANNEL, ctrl)
            control.name = 'Ctrl_' + str(control)
            self._ctrl_map.append(control)
        self._note_map.append(None)

        for ctrl in range(128):
            control = SliderElement(types.CC, SLIDERCHANNEL, ctrl)
            control.name = 'Ctrl_' + str(ctrl)
            self._ctrl_map.append(control)
        self._ctrl_map.append(None)
