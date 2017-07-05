from sqlalchemy import (
    Column,
    Integer,
    Unicode,
)

from .meta import Base


class Billionaire(Base):
    __tablename__ = 'billionaires'
    rank = Column(Integer, primary_key=True)
    name = Column(Unicode)
    age = Column(Integer)
    net_worth = Column(Integer)
    source = Column(Unicode)
    country = Column(Unicode)

    def to_json(self):
        output = {}
        output['rank'] = self.id
        output['name'] = self.title
        output['age'] = self.body
        output['net_worth'] = self.net_worth
        output['source'] = self.source
        output['country'] = self.country
        return output
