import url_graber
import downloader
import crawl_parser
from repo import SitesRepo, PageRepo, WordpairsRepo, Repo
import time
import os
import async_download

page_parser = crawl_parser.HtmlParser()
url_handler = url_graber.SitemapGruber()
download = downloader.Downloader()
sites = SitesRepo()
pages = PageRepo()
wordpairs = WordpairsRepo()

base_repo = Repo()


def main():
    os.chdir(r'/tmp')
    url_tuple_list = pages.get_not_scan_urls()
    url_list = [ url.url for url in url_tuple_list]
    async_download.async_download(url_list)

if __name__ == "__main__":
    main()


'''
    while True:
        site_list = sites.get_all()
        for site in site_list:
            url_list = url_handler.get_url_from_sitemap(site.name)
            pages.add_url(url_list, site.id)




for url_tuple in url_tuple_list:
            query_tuple_list = wordpairs.get_query()
            file = download.download_file(url_tuple.url)
            print(url_tuple)
            if file:
                pages.add_last_scan_date(url_tuple.id)
                page_parser.parse_html(file, query_tuple_list, url_tuple.id)
                os.remove(file)
            else:
                pages.del_bad_url(url_tuple.id)

        time.sleep(43200)

'''