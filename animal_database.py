""""Animal database WIP - unfinished"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class AnimalDatabase(Base):
    """ Define the Animal Database"""

    __tablename__ = "animals"
    id = Column(Integer, primary_key=True)
    species = Column(String)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __repr__(self):
        """ User-friendly description of the animal object. Can be invoked with str(object)."""
        return "({}, {}, {}, {})".format(self.name, self.breed, self.age, self.gender)


engine = create_engine("sqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)

# Populate the database with available animals for adoption:
sharo = AnimalDatabase(species='Dog', name='Sharo', breed='unbred', age=5, gender="male")
lucy = AnimalDatabase(species='Dog', name='Lucy', breed='collie', age=3, gender="Female")
daisy = AnimalDatabase(species='Dog', name='Daisy', breed='labrador', age=2, gender="fem")
rocco = AnimalDatabase(species='Dog', name='Rocco', breed='German Shepherd', age=1, gender="M")
duke = AnimalDatabase(species='Dog', name='Duke', breed='Doberman', age=4, gender="Male")
mike = AnimalDatabase(species='Dog', name='Mike', breed='Doberman', age=4, gender="Male")
max_ = AnimalDatabase(species='Dog', name='Max', breed='greyhound', age=7, gender="M")
bobby = AnimalDatabase(species='Dog', name='Bobby', breed='chow chow', age=6, gender='Unknown_gender')

maya = AnimalDatabase(species='Cat', name='Maya', breed='Sphynx', age=5, gender="F")
ruh = AnimalDatabase(species='Cat', name='Ruh', breed='unbred', age=3, gender="male")
tiger = AnimalDatabase(species='Cat', name='Tiger', breed='SAVANNAH', age=4, gender="M")

animal_pool = [sharo, lucy, daisy, rocco, duke, mike, max_, maya, ruh, tiger]

session = sessionmaker(bind=engine)()
for animal in animal_pool:
    session.add(animal)
session.commit()

query_response = session.query(AnimalDatabase)
dog_pool = query_response.filter_by(species='Dog').all()
cat_pool = query_response.filter_by(species='Cat').all()
