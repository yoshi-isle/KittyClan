from flask import Blueprint, jsonify, request
from services.member_service import MemberService

member_bp = Blueprint('member', __name__)
member_service = MemberService()

@member_bp.route('', methods=['GET'])
def get_all_members():
    members = member_service.get_all_members()
    if members:
        return jsonify(members), 200
    else:
        return jsonify({'message': 'Members not found'}), 404
    
@member_bp.route('/<member_id>', methods=['GET'])
def get_member(member_id):
    member = member_service.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'message': 'Member not found'}), 404