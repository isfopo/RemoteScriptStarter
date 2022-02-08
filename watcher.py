"""
  A helper class used to watch content changes in a file.
  From https://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes
"""

import os
import time


class Watcher(object):
    running = True
    refresh_delay_secs = 1

    def __init__(self, watch_file, callback=None):
        self._cached_stamp = 0
        self.filename = watch_file
        self.callback = callback

    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            if self.callback is not None:
                self.callback(self.filename)

    def watch(self):
        while self.running:
            try:
                time.sleep(self.refresh_delay_secs)
                self.look()
            except KeyboardInterrupt:
                print('\nStopped')
                break
            except FileNotFoundError:
                raise Exception("""
                File not found, check your version number
                and use 'Live {version} in the --version argument
                """)
                pass

