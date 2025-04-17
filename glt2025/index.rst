GLT 2025 Notes
==============

Message
-------

* E.g. task: wait interval, check. Very expressive: only procedural
  sleep() and check(), for that matter. Later: error handler, logger,
  usage of
  file:///home/jfasch/Documents/python-3.12.1-docs-html/library/asyncio-queue.html,
  watchdog task, ...

  but with await attached to the entry points into the asyncio
  internal callback system. jjj more see glt2024.

* This unifies both parallelism paradigms

  * Multithreading. 

    * Procedural therefore easy to understand. Details often
      overlooked:

      * Race conditions
      * Performance issues. Threads are relatively heavyweight in the
        OS, and IMO unnecessary when all threads *block* on events
        like timers and IO. Scheduling heavily involved, leading to
        latencies.

  * Callback oriented programming, with event loop (man select, poll,
    epoll), and callbacks for timer and IO events -> leads to object
    oriented programming to associate callbacks with data. not an easy
    job for, say, a single threaded web server handling many
    connections.

  This talk will show you how jjj blah

Implementation, Demo
--------------------

* Irrigator System Core. Only blocking device access
* D-Bus Object.

* Discuss watchdog simplicity: if one task hangs because a say I2C
  transaction (HW access like I2C is usually blocking), the watchdog
  task is not scheduled timely.
* Discuss error handling. Toplevel in task, show asyncio.Queue jjj

ToDo
----

* Doc, to include docstrings
* 

Links
-----

* https://dbus.freedesktop.org/doc/dbus-specification.html
* http://0pointer.net/blog/the-new-sd-bus-api-of-systemd.html
* sd-bus source code: https://github.com/python-sdbus/python-sdbus
* https://pypi.org/project/sdbus/
* https://apps.gnome.org/Dspy/
