from flask import Blueprint

applicant_bp = Blueprint('applicant', __name__)

@applicant_bp.route('', methods=['GET'])
def get_all_applicants():
    return "GET request to main function"