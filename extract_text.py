OUTPUT = """Retrieving speedtest.net configuration...
Testing from Webafrica (152.110.134.103)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by Technolutions (Cape Town) [0.26 km]: 3.616 ms
Testing download speed
Download: 82.22 Mbit/s
Testing upload speed
Upload: 96.04 Mbit/s"""


def main():
    global OUTPUT

    lines = OUTPUT.splitlines()
    for line in lines:
        if line.startswith("Download:"):
            download_speed = float(line.split()[1])
        elif line.startswith("Upload:"):
            upload_speed = float(line.split()[1])

    if download_speed < 90 or upload_speed < 90:
        email = "Doewnload speed is " + str(download_speed) + " Mbit/s and upload speed is " + str(upload_speed) + " Mbit/s"
        print(email)

if __name__ == '__main__':
    main()
