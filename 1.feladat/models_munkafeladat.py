from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional
from enum import Enum

class My_Time(BaseModel):
    todays_day: str
    todays_date: str