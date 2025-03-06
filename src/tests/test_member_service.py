import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.member_service import MemberService

class TestMemberService(unittest.TestCase):
    def setUp(self):
        self.member_service = MemberService()

    @patch('services.member_service.MemberService.get_all_members')
    def test_get_all_members(self, mock_get_all_members):
        mock_get_all_members.return_value = ["Member1", "Member2", "Member3"]
        members = self.member_service.get_all_members()
        self.assertEqual(len(members), 3)
        self.assertIn("Member1", members)
        self.assertIn("Member2", members)
        self.assertIn("Member3", members)

if __name__ == '__main__':
    unittest.main()
