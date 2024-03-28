from datetime import datetime

from models.enums import State
from schemas.base import BaseComplaint


class ComplaintOut(BaseComplaint):
    id: str
    photo_url: str
    created_at: datetime
    status: State
