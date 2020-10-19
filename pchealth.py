#! python3
import shutil
import psutil
from pyautogui import alert
from mymodules.speech import say
from mymodules.time import from_seconds
import os


def check_disk_usage_percent(min_percent=50):
    du_C = shutil.disk_usage('C:/')
    du_E = shutil.disk_usage('E:/')
    percent_free = (du_C.free + du_E.free)/(du_C.total + du_E.total)*100
    print("\n"+"[FREE DISK]".ljust(17) +
          f"{percent_free:.1f}%".ljust(14), end="")
    if percent_free < min_percent:
        return False
    return True


def check_disk_usage(min_absolute=250):
    du_C = shutil.disk_usage('C:/')
    du_E = shutil.disk_usage('E:/')
    gigabytes_free = (du_C.free + du_E.free) / 2**30
    print("[FREE DISK]".ljust(17) +
          f"{gigabytes_free:.1f} GB".ljust(14), end="")
    if gigabytes_free < min_absolute:
        return False
    return True


def check_cpu_usage(max_usage=50):
    usage = psutil.cpu_percent(10)
    print("\n"+"[CPU USAGE]".ljust(17) + f"{usage:.1f}%".ljust(14), end="")
    return usage < max_usage


def check_charging(min_charging=65):
    battery = psutil.sensors_battery()
    percent = battery.percent
    if battery.power_plugged:
        power = "PLUGGED IN"
        charging = True
    else:
        power = "ON BATTERY"
        charging = percent > min_charging

    print("\n"+"[PC-POWER]".ljust(17) + f"{power}".ljust(14), end="")
    print("-".rjust(4))
    _, hh, mm, ss = from_seconds(battery.secsleft)
    print("\n"+"[TIME-LEFT]".ljust(17) + f"{hh}:{mm}:{ss}".ljust(14), end="")
    print("-".rjust(4))
    print("\n"+"[BATTERY]".ljust(17) + f"{percent}%".ljust(14), end="")

    return charging


def check_reboot():
    """Returns True if the computer has a pending reboot."""
    # Only in linux
    return os.path.exists("/run/reboot-required")


def pc_health():
    say("Testing the health of your PC")
    print("\n"+"   TEST".ljust(17)+"RESULT".ljust(14)+" STATUS")
    total_tests = 4
    test_passed = 0
    suggestions = []
    if not check_disk_usage_percent():
        print("[FAILED]")
        suggestions.append("[FREE DISK] Free up some space\n")
    else:
        print("[PASSED]")
        test_passed += 1

    if not check_disk_usage():
        print("[FAILED]")
        suggestions.append("[FREE DISK] Free up some space\n")

    else:
        print("[PASSED]")
        test_passed += 1

    if not check_cpu_usage(75):
        print("[FAILED]")
        suggestions.append(
            "[CPU USAGE] Please End unimportant programs and tasks\n")
    else:
        print("[PASSED]")
        test_passed += 1

    if not check_charging(65):
        print("[FAILED]")
        suggestions.append("[BATTERY] Please Plug-In the charger\n")
    else:
        print("[PASSED]")
        test_passed += 1

    if test_passed == total_tests:
        say("Everything is OK", voice="F")
    else:
        a, b = '', ''
        if test_passed > 1:
            a = 's'
        if total_tests-test_passed > 1:
            b = 's'
        result = f"{test_passed} test{a} passed and {total_tests-test_passed} test{b} failed."
        say(result)
    return suggestions


if __name__ == '__main__':
    pc_health()
