from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Table,
)
from sqlalchemy.orm import relationship

from database.database import Base



class Talent(Base):
    __tablename__ = "talent"

    id = Column(String, primary_key=True)
    name = Column(String)
    grade = Column(String)


class Client(Base):
    __tablename__ = "client"

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String)
    industry = Column(String)


# required_skill = Table(
#     "required_skill",
#     Base.metadata,
#     Column("planning_id", Integer, ForeignKey("planning.id")),
#     Column("skill", String, ForeignKey("skills.name")),
# )
#
# optional_skill = Table(
#     "optional_skill",
#     Base.metadata,
#     Column("planning_id", Integer, ForeignKey("planning.id")),
#     Column("skill", String, ForeignKey("skills.name")),
# )


class Skills(Base):
    __tablename__ = "skills"

    name = Column(String, primary_key=True)
    category = Column(String)
    # skills_required = relationship(
    #     "Planning", secondary=required_skill, back_populates="required_skills"
    # )
    # skills_optional = relationship(
    #     "Planning", secondary=optional_skill, back_populates="optional_skills"
    # )


class Planning(Base):
    __tablename__ = "planning"

    id = Column(Integer, primary_key=True, nullable=False)
    original_id = Column(String, unique=True, nullable=False)
    talent_id = Column(String, ForeignKey("talent.id"))
    talent = relationship("Talent", foreign_keys=[talent_id])
    booking_grade = Column(String)
    operating_unit = Column(String, nullable=False)
    office_city = Column(String)
    office_postal_code = Column(String, nullable=False)
    job_manager_id = Column(String, ForeignKey("talent.id"))
    job_manager = relationship("Talent", foreign_keys=[job_manager_id])
    total_hours = Column(Float, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    client_id = Column(String, ForeignKey("client.id"))
    client_name = relationship("Client", foreign_keys=[client_id], viewonly=True)
    industry = relationship("Client", foreign_keys=[client_id])
    is_unassigned = Column(Boolean)

    # required_skills = relationship(
    #     "Skills", secondary=required_skill, back_populates="skills_required"
    # )
    # optional_skills = relationship(
    #     "Skills", secondary=optional_skill, back_populates="skills_optional"
    # )
