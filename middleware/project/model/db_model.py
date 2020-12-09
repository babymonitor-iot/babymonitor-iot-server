from project import db
from datetime import datetime


class BabyMonitor(db.Model):
    """ type: status or notification """

    __tablename__ = "baby_monitor"
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    crying = db.Column(db.Boolean, nullable=False)
    sleeping = db.Column(db.Boolean, nullable=False)
    breathing = db.Column(db.Boolean, nullable=False)
    time_no_breathing = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(80), nullable=False)
