from main import db

class ProjectPhase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phase_details = db.Column(db.String(600), nullable=True)
    phase_weight = db.Column(db.Integer, nullable=False)
    phase_status = db.Column(db.Boolean, nullable=False)
    #subphases = db.relationship('ProjectSubphase', backref='ProjecyPhase', lazy=True)

    def __init__(self, phase_details, phase_weight, phase_status):
        self.phase_details = phase_details