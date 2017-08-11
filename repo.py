from model import Persons
from model import Sites
from model import Pages
from model import PersonsPageRank
from model import Wordpairs
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError


class Repo():

    def __init__(self):
        self.engine = create_engine('mysql+pymysql://Crawler:probation2016@178.218.115.116:64004/GeeksTricks2?charset=utf8',echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def data_commit(self):
        self.session.commit()


class PersonsRepo(Repo):

    def get_all(self):
        payload_list = self.session.query(Persons).all()
        return payload_list


class SitesRepo(Repo):

    def get_all(self):
        payload_tuple = self.session.query(Sites.id, Sites.name).all()
        return payload_tuple


class PageRepo(Repo):
    def get_all(self):
        payload_tuple = self.session.query(Pages).all()
        return payload_tuple

    def add_url(self, url, id_site):
        '''
        bullet = Pages(url=url, site_id=id_site,
                       found_date_time="{0:%Y-%m-%d %H:%M:%S}".format(
                           datetime.utcnow()))
        try:
            self.session.add(bullet)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
        '''
        if self.session.query(Pages).filter(Pages.url == url).first():
            pass
        else:
            bullet = Pages(url=url, site_id=id_site,
                       found_date_time="{0:%Y-%m-%d %H:%M:%S}".format(
                           datetime.utcnow()))
            self.session.add(bullet)
            self.session.commit()

    def add_last_scan_date(self, id_url):
        scan_date = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.utcnow())
        self.session.query(Pages).filter_by(id=id_url).update(
            {'last_scan_date': scan_date})
        self.session.commit()

    def get_not_scan_urls(self):
        result_set = self.session.query(Pages.id, Pages.url).filter(
            or_(Pages.last_scan_date == None, Pages.last_scan_date +
                timedelta(days=1) < datetime.utcnow())).all()
        return result_set



class PersonsPageRankRepo(Repo):
    def add_rank(self, count, id_url, id_persons):
        if self.session.query(PersonsPageRank).filter(
                        PersonsPageRank.page_id == id_url).filter(
                        PersonsPageRank.person_id == id_persons).all():
            pass
        else:
            bullet = PersonsPageRank(rank=count, page_id=id_url,
                                     person_id=id_persons)
            self.session.add(bullet)
            self.session.commit()


class WordpairsRepo(Repo):
    def get_query(self):
        result_tuple_list = self.session.query(Wordpairs).all()
        return result_tuple_list
