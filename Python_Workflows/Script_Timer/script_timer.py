# add function and imports at the beginning of each script. Add time_stop.set() at end of script.

import threading
import time

def start_timer():
    t0 = time.time()
    stop = threading.Event()

    def tick():
        while not stop.is_set():
            elapsed = int(time.time() - t0)
            mins, secs = divmod(elapsed, 60)
            print(f"\rElapsed {mins}:{secs:02d}", end=" | ", flush=True)
            stop.wait(1)
        print()
    threading.Thread(target=tick, daemon=True).start()
    return stop

timer_stop = start_timer()

timer_stop.set()
