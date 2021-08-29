import unittest
from ps.restore_ip_addresses import restore_ip_addresses


class IpAddressRestorationTester(unittest.TestCase): 

    def test_25525511135(self):
        self.assertListEqual(restore_ip_addresses('25525511135'),
                             ["255.255.11.135", "255.255.111.35"])
        
    def test_9999(self):
        self.assertListEqual(restore_ip_addresses('9999'),
                             ["9.9.9.9"])

        
if __name__ == "__main__":
    unittest.main()
