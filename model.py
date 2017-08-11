from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base()


# Создаем класс для каждой таблицы
class Persons(Base):
    __tablename__ = 'Persons'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Person '{}'>".format(self.name)

    def __init__(self, name):
        self.name = name


class Wordpairs(Base):
    __tablename__ = 'Wordpairs'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    keyword_1 = Column(String(255), nullable=False)
    keyword_2 = Column(String(255), nullable=False)
    distance = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('Persons.id'), nullable=False)

    def __repr__(self):
        return "<KeyWord1 '{}', KeyWord2 '{}', Distance '{}', PersonID '{}'>".format(
                    self.keyword_1,
                    self.keyword_2,
                    self.distance,
                    self.person_id
                    )

    def __init__(self, keyword_1, keyword_2, distance, person_id):
        self.keyword_1 = keyword_1
        self.keyword_2 = keyword_2
        self.distance = distance
        self.person_id = person_id


class Sites(Base):
    __tablename__ = 'Sites'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Site '{}'>".format(self.name)

    def __init__(self, name):
        self.name = name


class Pages(Base):
    __tablename__ = 'Pages'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    url = Column(String(255), unique=True, nullable=False)
    site_id = Column(Integer, ForeignKey('Sites.id'), nullable=False)
    found_date_time = Column(DateTime)
    last_scan_date = Column(DateTime, default=None)

    def __repr__(self):
        return "<Url '{}', SiteID '{}', FoundDateTime '{}', LastScanDate '{}'>".format(
                    self.url,
                    self.site_id,
                    self.found_date_time,
                    self.last_scan_date
                    )


class PersonsPageRank(Base):
    __tablename__ = 'PersonsPageRank'

    rank = Column(Integer, nullable=False)
    page_id = Column(Integer, ForeignKey('Pages.id'), primary_key=True, nullable=False)
    person_id = Column(Integer, ForeignKey('Persons.id'), primary_key=True, nullable=False)

    def __repr__(self):
        return "<Rank '{}', PageID '{}', PersonID '{}'>".format(
                    self.rank,
                    self.page_id,
                    self.person_id
                    )

    def __init__(self, rank, page_id, person_id):
        self.rank = rank
        self.page_id = page_id
        self.person_id = person_id


class Users(Base):

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    login = Column(String(255), unique=True, nullable=False)
    pass_hash = Column(String(255), nullable=False)
    role = Column(Integer)

    def __init__(self, login, pass_hash, role):
        self.login = login
        self.pass_hash = pass_hash
        self.role = role

    def __repr__(self):
        return '<ID : {0} Login: {1} Password hash: {2}'.format(
            self.id,
            self.login,
            self.pass_hash
            )