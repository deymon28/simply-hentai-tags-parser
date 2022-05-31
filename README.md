# simply-hentai-tags-scraper-parser
simply-hentai tags scraper/parser

This is a program that receives tags from simply-hentai and writes them to a file.

Tags are scanned from the largest number of manga to the smallest. By changing the second range parameter on line 19 of the code, you change the number of pages to be scanned and in the same way limit the number of manga you need per tag.

To get all the tags, you need to find out the number of the last page with tags and add 1 to it, then enter this number in the second range parameter on line 19 of the code.
