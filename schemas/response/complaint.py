from datetime import datetime
from schemas.base import BaseComplaint

from models.enums import State


class ComplaintOut(BaseComplaint):
    id: str
    created_at: datetime
    status: State
