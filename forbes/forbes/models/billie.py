from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    BigInteger,
)

from .meta import Base


class Billionaire(Base):
    __tablename__ = 'billionaires'
    rank = Column(Integer, primary_key=True)
    name = Column(Unicode)
    age = Column(Integer)
    networth = Column(BigInteger)
    source = Column(Unicode)
    country = Column(Unicode)

    def to_json(self):
        output = {}
        output['rank'] = self.id
        output['name'] = self.title
        output['age'] = self.age
        output['networth'] = self.networth
        output['source'] = self.source
        output['country'] = self.country
        return output
