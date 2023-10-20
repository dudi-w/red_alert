from alarm_player import AlarmPlayer
from loop_timing import loopTiming
from alert_manager import alertManager

if __name__ == "__main__":
    alert_manager = alertManager(location=None,date_threshold=100)
    loop_timing = loopTiming(updates_per_second=1)
    alarm = AlarmPlayer('alarm-1-with-reverberation-30031.mp3')

    while True:
        alerts = alert_manager.alerts_to_json()
        new_alerts = alert_manager.look_for_new_alerts(alerts)
        if new_alerts:
            for alert in new_alerts:
                print(alert)
            alarm.play_alarm()
        loop_timing.end_loop()
