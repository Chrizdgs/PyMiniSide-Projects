# mapit.py - Launches a map in the browser using an address from the command line or clipboard
import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'Spain']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'Spain'] -> '870 Valencia St.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# Open the web browser to the Google Maps page for the address
# 'https://www.google.com/maps/place/<ADDRESS>'
webbrowser.open('https://www.google.com/maps/place/' + address)
