import time

class loopTiming:
    def __init__(self, updates_per_second: float) -> None:
        self._required_loop_duration = updates_per_second
        self._loop_start_time = time.time()

    def end_loop(self):
        time.sleep(0.1)
        return
        # current_loop_duration = time.time() - self._loop_start_time

        # if current_loop_duration < self._required_loop_duration:
        #     time.sleep(self._required_loop_duration - current_loop_duration)

        # self._loop_start_time = time.time()
