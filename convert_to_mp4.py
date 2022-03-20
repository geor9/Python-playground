# convert any video file to mp4

import os;

# print intro text
class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
print(f"Prerequisites: {bcolors.BOLD}brew install handbrakeCLI{bcolors.ENDC}")
print("\nStarting...")

# start again after completion
while True:
    #input file
    print("\nDrag the file into terminal, then hit Enter\n")
    pathname = input().strip('\'')
    print(pathname)

     # check if input file exists
    if os.path.isfile(pathname):
        print(f"\nConverting {pathname}")
    else:
        print("\nInput file "+pathname+" does not exist")
        continue

    # strip to filename from path
    from pathlib import Path; filename = Path(pathname).stem

    # convert file to mp4
    os.system('/opt/homebrew/bin/handbrakeCLI -i '+pathname+' -o ~/Desktop/'+filename+'_converted.mp4')

    # check if converted file exists
    if os.path.isfile(os.path.expanduser('~')+'/Desktop/'+filename+'_converted.mp4'):
        print(f"\nFile converted to ~/Desktop/{filename}_converted.mp4")
    else:
        print("\nFile not converted")