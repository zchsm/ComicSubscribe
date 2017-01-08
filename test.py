from crawler.comic import Comic
from crawler.crawler import save_image

comic = Comic()

comic_url = "http://www.dm5.com/manhua-guanlangaoshouquanguodasaipian-quancai/"
# comic_url = "http://manhua.dmzj.com/yiquanchaoren/"

chapter_dict = comic.get_comic(comic_url)
chapter_url = list(chapter_dict.keys())[0]

image_list = comic.get_chapter(comic_url, chapter_url)
image_url = image_list[0]

image_data = comic.get_image(chapter_url, image_url)
save_image(image_data["filename"], image_data["data"])
