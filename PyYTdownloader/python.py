# Welcome this is very simple python youtube installer
import pytube


print('Hello this is a project made by: Gabriel Dias')
print("""    / \__
  (    @\___
  /         O
 /   (_____/
/_____/   U""")
print('Please Read the Readme file for more instruction')
link = input('Welcome Please enter youtube video URL? \n ')
print('Please Choice 1-Highest Quality 2-Lowest 3-Audio Only? ')
choice = int(input())
# this is def the functions

    # function for the hightest
def get_highest():
    yt = pytube.YouTube(link)
    yt.streams.get_highest_resolution().download()
    title = str(yt.title)
    print('Your download is done!\n',title)
# function for the lowest
def get_lowest():
    yt = pytube.YouTube(link)
    title = str(yt.title)
    yt.streams.get_lowest_resolution().download()
    print('Your download is done!\n',title)
    
# function for the audio only
def get_audio():
    yt = pytube.YouTube(link)
    yt.streams.get_audio_only().download()
    title = str(yt.title)
    print('Your download is done!\n',title)


# if statment 
if choice ==1:
    get_highest()
elif choice ==2:
    get_lowest()    
elif choice ==3:
    get_audio()

else:
    print('ERROR You have entered the wrong choice::::: use numbers only')