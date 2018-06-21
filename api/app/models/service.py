from flask_restplus import fields
from qsystem import api, db
from .base import Base 
from .office import Office
from sqlalchemy import BigInteger, Integer, String, DateTime

class Service(Base):

    service_metadata  = db.Table('service_metadata',
                            db.Column('service_id', db.Integer, 
                                      db.ForeignKey('service.service_id'), primary_key=True, nullable=False),
                            db.Column('metadata_id', db.Integer,
                                      db.ForeignKey('metadata.metadata_id'), primary_key=True, nullable=False)
    )

    service_id              = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    service_code            = db.Column(db.String(50), nullable=False)
    service_name            = db.Column(db.String(500), nullable=False)
    service_desc            = db.Column(db.String(2000), nullable=False)
    parent_id               = db.Column(db.Integer, db.ForeignKey('service.service_id'), nullable=True)
    deleted                 = db.Column(db.DateTime, nullable=True)
    prefix                  = db.Column(db.String(10), nullable=False)
    display_dashboard_ind   = db.Column(db.Integer, nullable=False)
    actual_service_ind      = db.Column(db.Integer, nullable=False)

    offices                 = db.relationship("Office", secondary=Office.office_service, back_populates="services")
    service_reqs            = db.relationship('ServiceReq', backref='service', lazy=False)
    #services            = db.relationship('Service', backref='parent', lazy=False)
    # meta data is a reserved sqlalchemy keyword
    #metadatas           = db.relationship("Metadata", secondary=service_metadata, back_populates="services")

    def __repr__(self, service_name):
        return '<Service Name: %r>' % self.service_name

    def __init__(self, **kwargs):
        super(Service, self).__init__(**kwargs)
