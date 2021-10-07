import datetime
from sqlalchemy import Table, Column, Integer, DateTime, Sequence, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from flask_login import UserMixin
from geoalchemy2 import Geometry


engine = create_engine(
    'postgresql://mm:mm@localhost:5432/mysterymeeting')
base = declarative_base()
# session = sessionmaker(bind=engine)
# s = Session()
# session.query(User).filter_by(username='ahunt').first()

def getCursor():
    return Session(bind=engine)

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    lastip = Column(String)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(id={}, username={})>".format(self.id, self.username)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


class Location(base):
    __tablename__ = 'location'
    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    location = Column(Geometry)
    userid = Column(Integer, ForeignKey('users.id'))
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<UserLocation(id={}, useride={})>".format(self.id, self.userid)

class MysteryEvent(base):
    __tablename__ = 'event'
    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String)
    venue = Column(Integer, ForeignKey('venue.id'))
    meeting_time = Column(DateTime)
    attended = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<MysteryEvent(id={}, name={})>".format(self.id, self.name)

class Venue(base):
    __tablename__ = 'venue'
    id = Column(Integer, Sequence('venue_id_seq'), primary_key=True)
    name = Column(String)
    address = Column(String)
    hours = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Venue(id={}, name={})>".format(self.id, self.name)

class LocationKey(base):
    __tablename__ = 'location_key'
    id = Column(Integer, Sequence('location_key_id_seq'), primary_key=True)
    userid = Column(Integer, ForeignKey('users.id'))
    key = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<LocationKey(userid={}, key={}>".format(self.userid, self.key)

