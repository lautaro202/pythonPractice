from plyer import notification
title = 'A darle atomos!'
message = 'está moy boeno'
notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=10,
                    toast=False)
