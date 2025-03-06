from flask import Flask

from routes.member_routes import member_bp
from routes.applicant_routes import applicant_bp

from services.member_service import MemberService
from services.applicant_service import ApplicantService

app = Flask(__name__)

app.register_blueprint(applicant_bp, url_prefix='/applicant')
app.register_blueprint(member_bp, url_prefix='/member')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)