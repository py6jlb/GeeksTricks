from urllib import request
import shutil
import re
import gzip
import os


class Downloader():

    def _ungz_file(self, file_name):
        out_file_name = str(re.findall(r'(.+)\..{2,4}', file_name)[0])
        with gzip.open(file_name, 'rb') as archive, \
                open(out_file_name, 'wb') as target_file:
            shutil.copyfileobj(archive, target_file)
        os.remove('file_name')
        return out_file_name

    def download_file(self, url):
        split_url = url.split('/')
        if split_url[-1]:
            name = split_url[-1]
        else:
            name = split_url[-2]
        # try download file
        try:
            with request.urlopen(url) as response, open(name, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                if name.endswith('.gz'):
                    file_name = self._ungz_file(name)
                    return file_name
                else:
                    return name
        except:
            return False
