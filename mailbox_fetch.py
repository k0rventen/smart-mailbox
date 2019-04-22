import bluetooth
import time

arduino = "<Your HC-05 MAC address here>"

def twitter_notify():
    """
    Sends a DM via twitter to the specified twitter_id
    """
    import twitter
    twitter_id="<Your twitter ID>"
    api = twitter.Api(consumer_key="",
                  consumer_secret="",
                  access_token_key="",
                  access_token_secret="")

    api.PostDirectMessage("Mail is here !",twitter_id)


def fetch_mailbox():
    """connect to the arduino and retrieve the mailbox status

    Returns:
    - 2 if an error occured (could not connect to the mailbox)
    - 1 if one of the sensor is blocked -> there is mail
    - 0 if all the sensors returned a value above 0 -> no mail
    """
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((arduino,1))
        data = ""
        sock.send("?")
        while ";" not in data:
            data += sock.recv(1024)
        sock.close()
    except Exception as e:
        print e.args
        return 2

    data = data.replace(";","")
    vals = data.split(",")

    if "0" in vals:
        return 1
    return 0


def main():
    # Here we do the test 5 times in a row
    # to have some fault tolerance, in case
    # one of the sensor goes wild
    results=[]
    for i in range(5):
        results.append(fetch_mailbox())
        time.sleep(2)


    if results.count(1) is 5:
        # There is mail, do stuff !

        # Uncomment for twitter integration
        # twitter_notify()
        pass
    else:
        # No mail
        pass

if __name__ == "__main__":
    main()