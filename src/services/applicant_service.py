from typing import List

class ApplicantService:
    def __init__(self):
        pass

    def get_all_applicants(self) -> List[str]:
        return ["Applicant1", "Applicant2", "Applicant3"]

    def create_applicant(self, discord_id: int):
        pass

    def update_questionnaire(self, discord_id: int, questionnaire: List[str]):
        pass

    def cancel_application(self, discord_id: int):
        pass