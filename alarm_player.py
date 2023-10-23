import datetime
import threading
from pydub import AudioSegment
from pydub.playback import play


class AudioFormatError(Exception):
    pass


class AlarmPlayer:
    def __init__(self, audio_path: str = None, alarm_duration: int = 10):
        if audio_path is None or audio_path.endswith('.mp3'):
            self._audio_path = audio_path
        else:
            raise AudioFormatError(
                f"Check the filename extension: {audio_path}")
        self._alarm_duration = alarm_duration

    def _play_audio(self):
        sound = AudioSegment.from_file(self._audio_path, format="mp3")
        play(sound[:self._alarm_duration * 1000])

    def play_alarm(self):
        print("Current time:", datetime.datetime.now())
        if self._audio_path:
            audio_thread = threading.Thread(target=self._play_audio)
            audio_thread.start()
