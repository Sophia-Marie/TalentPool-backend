from app import db


class TempTP(db.Model):
    __tablename__ = 'temptp'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    forename = db.Column(db.String(80), unique=True, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80))
    telephoneNumber = db.Column(db.Integer)
    address = db.Column(db.String(200))
    desiredPosition = db.Column(db.String(100))
    # earliest starting date
    startingDate = db.Column(db.Date)
    graduation = db.Column(db.String(100), nullable=False)
    apprenticeship = db.Column(db.String(100))
    timestamp = db.Column(db.TIMESTAMP, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    started = db.Column(db.Boolean, default=True)
    languageTable = db.relationship('Languages', backref='temptp', lazy=True)
    studiesTable = db.relationship('Studies', backref='temptp', lazy=True)
    itSkillsTable = db.relationship('ItSkills', backref='temptp', lazy=True)
    furtherEducationTable = db.relationship('ItSkills', backref='temptp', lazy=True)

    def __repr__(self):
        return '<TempTP %r>' % self.username


class FurtherEducation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    education = db.Column(db.String(100))
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class Studies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studies = db.Column(db.String(100))
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class ItSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    itSkills = db.Column(db.String(100))
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


class Languages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(80), nullable=False)
    # knowledge how good you speak it:
    ability = db.Column(db.Integer, nullable=False)
    temptp_id = db.Column(db.Integer, db.ForeignKey('temptp.id'), nullable=False)


def list():
    return [TempTP, Languages]
