#!/usr/bin/python3
from sqlalchemy import Table, Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

# Association table for the Many-To-Many relationship between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'
    # Assuming other attributes of the Place model are defined here
    amenities = relationship("Amenity", secondary=place_amenity, back_populates="place_amenities", viewonly=False)

    @property
    def amenities(self):
        """FileStorage: Getter attribute amenities that returns the list of Amenity instances"""
        from models import storage
        return [amenity for amenity in storage.all(Amenity).values() if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """FileStorage: Setter attribute amenities that adds an Amenity.id to the amenity_ids"""
        if type(obj).__name__ == 'Amenity':
            self.amenity_ids.append(obj.id)

