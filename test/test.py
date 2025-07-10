import unittest
from rebuild_ticket_nbr_test import rebuild_ticket_nbr

class TestRebuildTicketNumber(unittest.TestCase):
    
    def test_e2_s_1234(self):
        self.assertEqual(rebuild_ticket_nbr("[release-8.2.2] e2 1234"), 'EEV2-1234')
        
    def test_eev2_dash_5678(self):
        self.assertEqual(rebuild_ticket_nbr("fixed bug in EEV2-5678"), 'EEV2-5678')
        
    def test_eev2_space_5678(self):
        self.assertEqual(rebuild_ticket_nbr("fixed bug in EEV2 5678"), 'EEV2-5678')
        
    def test_ev2_9012(self):
        self.assertEqual(rebuild_ticket_nbr("some commit EV2 9012"), 'EEV2-9012')

    def test_e2_dash_3456(self):
        self.assertEqual(rebuild_ticket_nbr("refs E2-3456"), 'EEV2-3456')
        
    def test_eeev2_7890(self):
        self.assertEqual(rebuild_ticket_nbr("bugfix EEEV2 7890"), 'EEV2-7890')

    def test_ev2_dash_1001(self):
        self.assertEqual(rebuild_ticket_nbr("merge EV2-1001"), 'EEV2-1001')

    def test_eev2_no_dash(self):
        self.assertEqual(rebuild_ticket_nbr("working on EEV2 4321"), 'EEV2-4321')

    def test_missing_v(self):
        self.assertEqual(rebuild_ticket_nbr("refactoring EE2 4321"), 'EEV2-4321')

    def test_extra_v(self):
        self.assertEqual(rebuild_ticket_nbr("patch EEVV2 9999"), 'EEV2-9999')

    def test_no_dash(self):
        self.assertEqual(rebuild_ticket_nbr("fix EEV21234"), 'EEV2-1234')

if __name__ == '__main__':
    unittest.main(verbosity=2)
