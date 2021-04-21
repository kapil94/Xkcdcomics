# Xkcdcomics
to get and download comic images from Xkcd website

program requires requests,bs4 module to work.

Algorithm

1. request a xkcd url and get a response in form od bs4object.
2. get image in div with id "comic" and store it in a list.
3. check length of image list if it is greater than 0 then get src url and append in image_url list.
4. Now,from bs4 object check anchor tag with rel=prev and get its url from href.
5. Modify,xkcd url and call function getImageUrl until xkcd url endswith="#" (Their is no previous page left).
6. Traverse urls stored in image_urls,get and download images from those urls at one location.
