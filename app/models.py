from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

import sqlalchemy as sa
import sqlalchemy.orm as so


class Base(DeclarativeBase):
    pass

"""Database for the hedgehogs including their name, age, and staff member. """

class Hedgehogs(Base):
    __tablename__ = 'hedgehogs'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(), nullable= False)
    age: Mapped[int] = mapped_column(sa.Integer(), nullable= True)
    staff_member: Mapped[int] = ForeignKey('staff.id')
    # Need to add a relationship to the staff for many to one. Many hedgehogs but only one staff member.

""" Databases for the staff members including the volunteers and permanent staff. """

class Staff():
    __tablename__ = 'staff'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key= True)
    name: Mapped[str] = mapped_column(sa.String(), nullable= False)
    hedgehog_under_care: Mapped[int] = ForeignKey('hedgehogs.id')

class VolunteerStaff():
    
    __tablename__ = 'volunteer_staff'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key= True)
    hours: Mapped[int] = mapped_column(sa.Integer(), nullable= False)

class PermanentStaff(Staff):
    __tablename__ = 'permanent_staff'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key= True)
    years_of_experience: Mapped[int] = mapped_column(sa.Integer(), nullable= False)

"""Databases for all things related to the login and registration of the users"""

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('Sign In')

