#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy import *


metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """ getter for reviews """
        reviews = []
        allreviews = models.storage.all(Review)
        for item in allreviews.values():
            if item.place_id == self.id:
                reviews.append(item)
        return reviews

    @property
    def amenities(self):
        """ getter for amenities """
        amenities = []
        allamen = models.storage.all(Amenity)
        for item in allamen.values():
            if item.amenity_ids == self.id:
                amenities.append(item)
        return amenities

    @amenities.setter
    def amenities(self):
        """ setter for amenities """
        self.amenity_ids.append(Amenity.id)
