# Argparse assignment 
# 1: Create a cli program to take 2 arguments: url (required) and destination_file (optional)
# 2: Create a description of what the program does
# 3: Implement the download part
# 4: If no destination file was specified, save the file in default_file.dat
# 5: Improve the code: if no destination file was specified, use the last subset of the URL as the name for the file
# 6:Improve the code: if no destination file was specified, use the MIME-type of the HTTP header to guess the file extension

import argparse
from modules import webget

from modules.webget import download

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination', help='The name of the file to store the url in')
    # default = 'default_file.dat',

    args = parser.parse_args()
    print('URL:', args.url)
    print('Destination:', args.destination)

    webget.download(args.url, args.destination)

    if args.destination == NONE:
        destination = args.url.replace('http://', '').strip('.com') + 'dat'
        webget.download(args.url, destination)
    else:
        webget.download(args.url, args.destination)