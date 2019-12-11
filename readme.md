## Mangakyo[dot].com Scrapping

### How to use

run this spider, you can crawl multiple manga by parsing comma delimiter to `url` arguments
```
scrapy crawl mangakyoweb -a "urls=https://www.mangakyo.com/manga/boku-no-hero-academia/,https://www.mangakyo.com/manga/dr-stone/"
```

in `settings.py` you need change `IMAGES_STORE` to taget location on your computer