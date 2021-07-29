from app import db

class Blogg(db.Model):
       __tablename__ = "nyheter"
       
       id = db.Column(db.Integer, primary_key=True)
       tittel = db.Column(db.String, nullable=False)
       nyhet = db.Column(db.String, nullable=False)
       forfatter = db.Column(db.String, nullable=False)
       """bruker_id = db.Column(db.Integer, db.ForeignKey('brukere.id'))"""

       def __init__(self, tittel, nyhet, forfatter):
              self.tittel = tittel
              self.nyhet = nyhet
              self.forfatter = forfatter
              """self.bruker_id = bruker_id"""

              def __repr__(self):
                     return '<tittel {}>'.format(self.body)

class Bruker(db.Model):
       __tablename__ = "brukere"

       id = db.Column(db.Integer, primary_key=True)
       brukernavn = db.Column(db.String, nullable=False)
       passord = db.Column(db.String, nullable=False)
       navn = db.Column(db.String, nullable=False)       
       """navn = db.relationship('nyheter', backref='person',lazy='dynamic')"""

       def __init__(self, brukernavn, passord, navn):
              self.brukernavn = brukernavn
              self.passord = passord
              self.navn = navn

              def __repr__(self):
                     return '<Bruker %r>' % self.brukernavn

