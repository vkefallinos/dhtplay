#!/usr/bin/python

import gtk

from ui.interface import Interface
import defaults

settings = "settings.cfg"

def start():
  gtk.gdk.threads_init()
  config = defaults.default_config
  config.read(settings)
  app = Interface(config)
  app.show()
  gtk.main()
  try:
    app.destroy()
  except:
    pass
  config.write(open(settings, 'w'))

if __name__ == "__main__":
  start()
