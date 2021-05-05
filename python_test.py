# Python function to report HTTP status codes of URL
# Usage: python python_test.py https://example.com

# Note that there's an alternate (and slightly cleaner) way of doing this using the `requests` module. But since that module must be installed separately, I've decided not to use it.

import argparse
import datetime
import time
import urllib.request
import urllib.error
import sys  

def main():

    # Define CLI Arguments (URL is required)
    parser = argparse.ArgumentParser()
    parser.add_argument('url', metavar='url', type=str, nargs='+', help='URL to monitor')
    args = parser.parse_args()

    print("Starting inifinite monitoring loop...")

    # To escape the infinite loop, use CTRL+C or another process termination method.
    while True:
        start = datetime.datetime.now()

        # Attempt to connect to URL. Exit if error is encountered.
        try:
           conn = urllib.request.urlopen(args.url[0])
        except (ValueError, urllib.error.URLError) as e:
            print(e)
            sys.exit()

        end = datetime.datetime.now()
        delta = end - start
        elapsed_seconds = round(delta.microseconds * .000001, 6)


        print ("---")
        print ("Time: " + str(start))
        print("HTTP Status Code: " + str(conn.getcode()))
        print("Response Time: " + str(elapsed_seconds) + " seconds")
        print ("---")

        # Wait 60 seconds before repeating
        time.sleep(60)

main()