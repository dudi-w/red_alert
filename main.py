from alarm_player import AlarmPlayer
from loop_timing import LoopTiming
from alert_manager import AlertManager

if __name__ == "__main__":
    import argparse

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="A simple Python program with command-line arguments.")

    # Define your command-line arguments
    parser.add_argument("-l", "--location", type=str, default=None,
                        help="Select a settlement name according to the alert area as it appears on the Home Front Command website https: //www.oref.org.il/, If no place is specified, this will alert the whole country")
    parser.add_argument("-t", "--threshold_history", type=int, default=10,
                        help="Setting minutes What is the threshold for the notification history, By default it is set to 10 minutes.")
    parser.add_argument("-u", "--updates_per_second", type=float, default=1,
                        help="Set the refresh rate of notifications in seconds, By default it is set to 1 second.")
    parser.add_argument("-f", "--file", type=str, default="alarm-1-with-reverberation-30031.mp3",
                        help="Specify a alarm file (in mp3 format).", required=True)
    parser.add_argument("-d", "--alarm_duration", type=int,
                        default=90, help="A flag without a value.")

    # Parse the command-line arguments
    args = parser.parse_args()

    alert_manager = AlertManager(
        location=args.location, date_threshold=args.threshold_history)
    loop_timing = LoopTiming(updates_per_second=args.updates_per_second)
    alarm = AlarmPlayer(args.file, args.alarm_duration)

    while True:
        new_alerts = alert_manager.look_for_new_alerts()
        if new_alerts:
            for alert in new_alerts:
                print(alert)
            alarm.play_alarm()
        loop_timing.end_loop()