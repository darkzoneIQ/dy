print("MAFIA SCRIPT")
print("download videos for youtube")
print("tele»@Ft_r5")
from pafy import new 
url = input("type link »»»:")
video = new(url)
stream = video.stream
for i in stream:
	print(i)
stream[0].download()