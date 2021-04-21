import bs4,requests
import sys,os


sys.setrecursionlimit(3000)  #recursion limit is 1000 ,setting  recursion list to process less than 3000 pages

url="https://xkcd.com/"
image_urls=[]

# to get images urls and store in a list
def getImageUrls():
	
	global image_urls,url
	
	while not url.endswith("#"):  
					
		res=requests.get(url)
		bs4Obj=bs4.BeautifulSoup(res.text,'html.parser')	

		Comic_images=bs4Obj.select('#comic img')
		
		if len(Comic_images)>0:
			image_urls.append("https:"+Comic_images[0].get('src'))
			
			prev=bs4Obj.select('a[rel=prev]')
			url="https://xkcd.com/"
			url+=prev[0].get('href')
			getImageUrls()
		else:
			prev=bs4Obj.select('a[rel=prev]')
			url="https://xkcd.com/"
			url+=prev[0].get('href')
			getImageUrls()


# to traverse the list of urls and download the images
def downloadImages():

	os.chdir('/home/kapil/Desktop/')
	os.makedirs('comicImages',exist_ok=True)
	os.chdir('/home/kapil/Desktop/comicImages')
	
	global image_urls
	
	for img in range(0,len(image_urls)):
		
		image_obj=open(image_urls[img][image_urls[img].index('comics')+7:],'wb')	
		
		for chunk in requests.get(image_urls[img]):
			
			image_obj.write(chunk)
		
		image_obj.close()
			
		
getImageUrls()
downloadImages()
