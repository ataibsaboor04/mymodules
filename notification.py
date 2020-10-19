from win10toast import ToastNotifier


def notify(title, text, path=None, time=30):
    toaster = ToastNotifier()
    if path is not None:
        toaster.show_toast(title, text+"\nAtaib-Saboor",
                           icon_path=path, duration=time)
    else:
        toaster.show_toast(title, text+"\nAtaib-Saboor",
                           duration=time)
