from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    tasks = relationship("Task", back_populates="owner")


# 中間テーブル: task_items
task_items = Table(
    'task_items',
    Base.metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True),
    Column('item_id', ForeignKey('items.id'), primary_key=True)
)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")
    items = relationship("Item", secondary=task_items, back_populates="tasks")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    status = Column(String(255), default="未完了")
    description = Column(String(255), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    tasks = relationship("Task", secondary=task_items, back_populates="items")
