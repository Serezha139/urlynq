from typing import List

from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    cutoffValue: float
    referralUserIdValue: float
    baseMutualContactsValue: float
    baseMutualEventsValue: float
    userId: str
    referralUserID: str
    prompt: str
    exclude: List[str]
    contacts: List[str]
    circles: List[str]
    events: List[str]
