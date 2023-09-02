import webbrowser, sys

if len(sys.argv) > 1:
    adress = ' '.join(sys.argv[1:])

else:
    print("Please Enter the adress")

webbrowser.open('https://www.google.com/maps/place/' + adress)