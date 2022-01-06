from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Table
from sqlalchemy import func
from sqlalchemy.orm import relationship

from .db import Base


userTasks = Table('task_users', Base.metadata,
                  Column('id', Integer, primary_key=True),
                  Column('task_id', ForeignKey('tasks.id')),
                  Column('user_id', ForeignKey('users.id'))
                  )


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())

    items = relationship("Item", back_populates="owner")
    tasks = relationship("Task", secondary=userTasks, back_populates="user")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String)
    flag = Column(String)
    state = Column(Boolean)

    url = Column(String)
    user = relationship("User", secondary=userTasks, back_populates="tasks")

