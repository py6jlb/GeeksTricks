import re
from reppy.cache import RobotsCache
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from repo import PersonsPageRankRepo


class SitemapParser():
    def get_sitemap_list(self, site):
        robots = RobotsCache()
        sitemaps = robots.sitemaps(site)
        return sitemaps

    def _gen_ns(self, tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    def _get_file_name(self, url):
        split_url = url.split('/')
        if split_url[-1]:
            name = split_url[-1]
        else:
            name = split_url[-2]
        return name

    def parse_sitemap(self, sitemapfile, tmp_file, site_id):
        tree = ET.parse(sitemapfile)
        root = tree.getroot()
        namespaces = {'ns': self._gen_ns(root.tag)}
        sitemaps = []
        for child in root:
            url = child.find('ns:loc', namespaces=namespaces).text
            name = self._get_file_name(url)
            if name.endswith('.xml') or 'sitemap' in name:
                sitemaps.append(url)
            else:
                tmp_file.write(url + '+!+' + str(site_id) + '\n')
        return sitemaps


class HtmlParser():
    def __init__(self):
        self.rank = PersonsPageRankRepo()

    def parse_html(self, html_file, query_tuple_list, id_url):
        if html_file.endswith('.xml') or html_file.endswith('.gz'):
            pass
        else:
            soup = BeautifulSoup(open(html_file))
            text = soup.get_text()
            for query in query_tuple_list:
                regul_distance = '\w+\s' * query.distance
                search_regul = re.compile('{0}\s{1}{2}\s|{2}\s{1}{0}\s'.format(
                                                query.keyword_1, regul_distance,
                                                query.keyword_2), re.IGNORECASE)
                count = len(re.findall(search_regul, text))
                if count:
                    self.rank.add_rank(count, id_url, query.person_id)
