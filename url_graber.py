from bs4 import BeautifulSoup
import crawl_parser
import downloader
import os


class SitemapGruber():
    def __init__(self):
        self.parser_sitemap = crawl_parser.SitemapParser()
        self.parser_robots = crawl_parser.RobotsParser()
        self.downloader = downloader.Downloader()

    def get_url_from_sitemap(self, site_url):
        sitemap_list = self.parser_robots.get_sitemap_list(site_url)
        url_list = []
        for sitemap in sitemap_list:
            file = self.downloader.download_file(sitemap)
            url_dict = self.parser_sitemap.parse_sitemap(file)
            sitemap_list.extend(url_dict['sitemap'])
            url_list.extend(url_dict['urls'])
            os.remove(file)
        return url_list


class SiteGruber():
    def __init__(self):
        self.downloader = downloader.Downloader()

    def get_url_from_html(self, site, url):
        pass