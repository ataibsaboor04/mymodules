import psutil
import sys
from win10toast import ToastNotifier


def seconds_to_hours(sec):
    mm, ss = divmod(sec, 60)
    hh, mm = divmod(mm, 60)
    return hh, mm, ss


def alert(text, percent, time=30):
    toaster = ToastNotifier()
    toaster.show_toast(
        text, f"Your battery is {percent}% charged\nAtaib Saboor", icon_path=f"E:/Python Programs/Images/battery.ico", duration=time)


def percent():
    battery = psutil.sensors_battery()
    print("Charge:", f"{battery.percent}%")
    hh, mm, ss = seconds_to_hours(battery.secsleft)
    return f"{hh}:{mm}:{ss}"


def main():
    battery = psutil.sensors_battery()
    percent = battery.percent
    if battery.power_plugged:
        if percent >= 95:
            alert("Please Plug-Out the Charger", percent)
        elif percent >= 88:
            main()

        sys.exit()
    else:
        if percent <= 35:
            alert("Please Plug-In the Charger", percent, 90)
        elif percent <= 60:
            alert("Please Plug-In the Charger", percent)
        sys.exit()


if __name__ == '__main__':
    main()
