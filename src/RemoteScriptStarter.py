from __future__ import with_statement

import Live

from _Framework.ControlSurface import ControlSurface


class RemoteScriptStarter(ControlSurface):
    def __init__(self, c_instance):
        with self.suppressing_rebuild_requests():
            ControlSurface.__init__(self, c_instance)
            live = Live.Application.get_application()
            self._live_major_version = live.get_major_version()
            self._live_minor_version = live.get_minor_version()
            self._live_bugfix_version = live.get_bugfix_version()

            # write your init code here

    def disconnect(self):
        """clean things up on disconnect"""
        ControlSurface.disconnect(self)
        return None
