import datetime
from sqlalchemy import Table, Column, Integer, DateTime, Sequence, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from flask_login import UserMixin
from geoalchemy2 import Geometry


engine = create_engine(
    'postgresql://mysterymeeting@localhost:5432/mysterymeeting')
base = declarative_base()
Session = sessionmaker(bind=engine)
# s = Session()
# s.query(User).filter_by(username='ahunt').first()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    last_login = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<User(id={}, username={})".format(self.id, self.username)

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


class UserLocation(base):
    __tablename__ = 'location'
    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    location = Column(Geometry('POLYGON'))
    userid = Column(Integer, ForeignKey('users.id'))
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<UserLocation(id={}, useride={})".format(self.id, self.userid)

class MysteryEvent:
    __tablename__ = 'mystery_event'
    id = Column(Integer, Sequence('mystery_event_id_seq'), primary_key=True)
    name = Column(String)
    venue = Column(String)
    meeting_time = Column(DateTime)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
