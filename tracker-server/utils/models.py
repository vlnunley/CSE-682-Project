from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional

class TrackerBaseModel(ABC):
    r"""Base class for type checking model"""

    @classmethod
    @abstractmethod
    def TABLE(cls) -> str:
        r"Database table backing the model"
        raise NotImplementedError
    
@dataclass(kw_only=True)
class User(TrackerBaseModel):
    TABLE: ClassVar[str] = "user"
    id: Optional[int] = None
    username: str
    password: str
    email: str
    phoneNumber: Optional[str] = None

@dataclass(kw_only=True)
class Habit(TrackerBaseModel):
    TABLE: ClassVar[str] = "habit"
    id: Optional[int] = None
    name: str
    classification: Optional[str] = None
    active: bool = True
    user: User

@dataclass(kw_only=True)
class Goal(TrackerBaseModel):
    TABLE: ClassVar[str] = "goal"
    id: Optional[int] = None
    name: str
    frequencyNum: int
    frequencyType: str
    habitId: int

@dataclass(kw_only=True)
class HabitEntry(TrackerBaseModel):
    TABLE: ClassVar[str] = "habit_entry"
    id: Optional[int] = None
    created_date: datetime
    note: Optional[str] = None
    status: str
    habitId: int
    goalId: int

@dataclass(kw_only=True)
class Mood(TrackerBaseModel):
    TABLE: ClassVar[str] = "mood"
    id: Optional[int] = None
    name: str

@dataclass(kw_only=True)
class MoodEntry(TrackerBaseModel):
    TABLE: ClassVar[str] = "mood_entry"
    id: Optional[int] = None
    created_date: datetime
    mood: Mood

@dataclass(kw_only=True)
class HabitMood(TrackerBaseModel):
    TABLE: ClassVar[str] = "habit_mood"
    id: Optional[int] = None
    mood: Mood
    habit: Habit
