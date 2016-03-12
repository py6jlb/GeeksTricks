import crawl_parser
import downloader
import os


class SitemapGruber():
    def __init__(self):
        self.parser_sitemap = crawl_parser.SitemapParser()
        self.downloader = downloader.Downloader()

    def get_url_from_sitemap(self, site_url, tmp_file, site_id):
        sitemap_list = self.parser_sitemap.get_sitemap_list(site_url)
        if sitemap_list:
            for sitemap in sitemap_list:
                file = self.downloader.download_file(sitemap)
                if file:
                    url_dict = self.parser_sitemap.parse_sitemap(file, tmp_file, site_id)
                    sitemap_list.extend(url_dict)
                    os.remove(file)
                else:
                    pass
        else:
            pass


class SiteGruber():
    def __init__(self):
        self.downloader = downloader.Downloader()

    def get_url_from_html(self, site, url):
        pass