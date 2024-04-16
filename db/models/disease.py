from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from db import Base


disease_symptoms = Table('disease_symptoms', Base.metadata,
                         Column('disease_id', Integer, ForeignKey('diseases.id', ondelete='CASCADE')),
                         Column('symptom_id', Integer, ForeignKey('symptoms.id', ondelete='CASCADE')))


class Disease(Base):
    __tablename__ = 'diseases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    symptoms = relationship("Symptom", secondary=disease_symptoms, back_populates="diseases")


class Symptom(Base):
    __tablename__ = 'symptoms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    diseases = relationship('Disease', secondary=disease_symptoms, back_populates='symptoms')
