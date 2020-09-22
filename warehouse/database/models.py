from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name


class Units(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    unit = Column(String(10), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return self.unit


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    unit = Column(Integer, ForeignKey('units.id'))
    category = Column(Integer, ForeignKey('categories.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Positions(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    position = Column(Integer, ForeignKey('positions.id'))

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return self.full_name


class Vendors(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ownership_form = Column(String(50), nullable=False)
    address = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)

    def __init__(self, name, ownership_form, address, phone, email):
        self.name = name
        self.ownership_form = ownership_form
        self.address = address
        self.phone = phone
        self.email = email

    def __repr__(self):
        return self.name
