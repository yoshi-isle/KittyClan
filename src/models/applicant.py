from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional

from bson import ObjectId


@dataclass
class Applicant:
    _id: Optional[ObjectId] = ObjectId()
    discord_id: int
    applicant_data: Optional[ObjectId]
    questionnaire: List[str]
    legacy_date: Optional[datetime]