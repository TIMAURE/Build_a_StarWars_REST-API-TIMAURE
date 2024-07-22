from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    

    def __repr__(self):
        return '<User %r>' % self.user_name

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            }
    
    class Planet(db.Model):
     __tablename__ = 'planet' 
    planet_id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(100), nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(100), nullable=True)
    terrain = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Planet %r>' % self.planet_name
    

    def serialize(self):
        return {
            "planet_id": self.planet_id,
            "planet_name": self.planet_name,
            "planet_climate": self.planet_climate,
            "planet_diameter": self.planet_diameter,
            "planet_terrain": self.planet_terrain,
        }
    

    class Characters(db.Model):
     __tablename__ = 'characters'
    characters_id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(100), nullable=False)
    character_weight = db.Column(db.String(100), nullable=True)
    character_hair_color = db.Column(db.String(20), nullable=True)
    character_eye_color = db.Column(db.String(20), nullable=False)
    character_birth_year = db.Column(db.Integer, nullable=False)
    

    homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.planet_id'), nullable=True)

    homeworld = db.relationship('Planet', backref='characters')
    


    def __repr__(self):
        return '<Character %r>' % self.characters_id

    def serialize(self):
        return {
            "characters_id": self.characters_id,
            "characters_name": self.character_name,
            "characters_birth_year": self.character_birth_year,
            "characters_eye_color": self.character_eye_color,
            "characters_hair_color": self.character_hair_color,
            "character_weight": self.character_weight,
            "homeworld": self.homeworld.charters_name if self.homeworld else None,
        }



class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)  
    user = db.relationship('User' , backref='favorites')
    
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.planet_id'), nullable=True)  
    planet = db.relationship('Planet', backref='favorites')
    
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.characters_id'), nullable=True)  
    characters = db.relationship('Character', backref='favorites')

def __repr__(self):
        return '<Favorite %r>' % self.id

def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }