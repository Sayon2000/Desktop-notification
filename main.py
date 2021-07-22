import time
from plyer import notification

notification_title = input("enter the title : ")
notification_message = input("enter the message : ")
notification_timeout = int(input("enter the timeout : "))
remind_after = int(input("enter the time gap : "))





if __name__ == "__main__":
    while True:
    
        notification.notify(
            title = notification_title,
            message = notification_message,
            timeout = notification_timeout

        )
        time.sleep(remind_after)