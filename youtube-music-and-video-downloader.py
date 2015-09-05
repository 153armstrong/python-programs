from bs4 import BeautifulSoup
import urllib,pafy


def spider( name ):
    url= "https://www.youtube.com/results?search_query="+ name
    print url
    r = urllib.urlopen(url)
    soup= BeautifulSoup(r,"html.parser")
    for link in soup.findAll('',{'class':'yt-lockup-title '}):
        x= str(link)
        y= x.find("href")
        url1= url + str(x[y+6:y+26])
        print url1
        save_to_computer(url1)
        break 


def save_to_computer(url_to_save):
    video= pafy.new(url_to_save)
    bestaudio= video.getbest("mp4") #saves only mp4 for now, but other formats to be incorporated 
    bestaudio.download('/home/keerthi/Music')
        
        
name= raw_input(" Enteer the name of the song and the artist(if possible) to download:")
spider ( name )
