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

import sqlalchemy as sa
import sqlalchemy.orm as so


class Base(DeclarativeBase):
    pass

class Hedgehogs(Base):
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(), nullable= False)
    age: Mapped[int] = mapped_column(sa.Integer(), nullable= True)
    staff_member: Mapped[int] = ForeignKey
    # Need to add a relationship to the staff for many to one. Many hedgehogs but only one staff member.

class Staff():
    __tablename__ = 'staff'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key= True)
    name: Mapped[str] = mapped_column(sa.String(), nullable= False)

class VolunteerStaff():
    
    __tablename__ = 'volunteer_staff'

class PermanentStaff(Staff):
    __tablename__ = 'permanent_staff'
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key= True)
    years_of_experience: Mapped[int] = mapped_column(sa.Integer(), nullable= False)
    #Need to link to how many hedgehogs are in each staff members care