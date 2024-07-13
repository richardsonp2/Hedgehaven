from __future__ import annotations

from typing import List, Optional

import sqlalchemy as sa
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped, mapped_column, relationship, registry

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

"""Databases for all of the user profiles including the staff members and the volunteers. """

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(sa.String(120), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(sa.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

"""Database for the hedgehogs including their name, age, and staff member. """

class Hedgehogs(db.Model):
    __tablename__ = 'hedgehogs'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(), nullable= False)
    age: Mapped[int] = mapped_column(sa.Integer(), nullable= True)
    staff_member: Mapped[int] = ForeignKey('staff.id')
    # Need to add a relationship to the staff for many to one. Many hedgehogs but only one staff member.

""" Databases for the staff members including the volunteers and permanent staff. """

class Staff(db.Model):
    __tablename__ = 'staff'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    hedgehog_under_care: Mapped[int] = mapped_column(ForeignKey('hedgehogs.id'))
    staff_type: Mapped[str] = mapped_column(String(50), nullable=False)  # Add type column for polymorphic identity

    __mapper_args__ = {
        'polymorphic_identity': 'staff',
        'polymorphic_on': staff_type
    }

class VolunteerStaff(Staff):
    __tablename__ = 'volunteer_staff'
    id: Mapped[int] = mapped_column(ForeignKey('staff.id'), primary_key=True)
    hours: Mapped[int] = mapped_column(Integer, nullable=False)
    staffkey: Mapped[int] = mapped_column(ForeignKey('staff.id'), use_existing_column=True)

    __mapper_args__ = {
        'polymorphic_identity': 'volunteer_staff',
        'inherit_condition': (id == Staff.id)
    }

class PermanentStaff(Staff):
    __tablename__ = 'permanent_staff'
    id: Mapped[int] = mapped_column(ForeignKey('staff.id'), primary_key=True)
    years_of_experience: Mapped[int] = mapped_column(Integer, nullable=False)
    staffkey: Mapped[int] = mapped_column(ForeignKey('staff.id'), use_existing_column=True)

    __mapper_args__ = {
        'polymorphic_identity': 'permanent_staff',
        'inherit_condition': (id == Staff.id)
    }