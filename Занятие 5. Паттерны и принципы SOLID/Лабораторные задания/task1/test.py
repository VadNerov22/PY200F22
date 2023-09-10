import unittest
from main import ProjectStorage


class MyTestCase(unittest.TestCase):
    def test_check_project(self):
        self.assertTrue(ProjectStorage.check_project({"project_id": 122245,
                                                        "project_type": 'ОВОС', "name": 'ТЭС-1', "price": 125474.78}))
        self.assertRaises(TypeError, ProjectStorage.check_project, "122245")
        self.assertRaises(ValueError, ProjectStorage.check_project, 125474)

    def test_add_project(self):
        p = {"project_id": 122245, "project_type": 'ОВОС', "name": 'ТЭС-1', "price": 125474.78}
        self.assertEqual(ProjectStorage.add_project(p), [{"project_id": 122245, "project_type": 'ОВОС',
                                                          "name": 'ТЭС-1', "price": 125474.78}, {}])

    def test_update_project(self):
        p_new = {"project_id": 122245, "project_type": 'ОВОС', "name": 'ТЭС-1 и ТП-4', "price": 177777.00}
        self.assertEqual(ProjectStorage.update_project(p_new), [{"project_id": 122245, "project_type": 'ОВОС',
                                                                 "name": 'ТЭС-1 и ТП-4', "price": 177777.00}, {}])

if __name__ == '__main__':
    unittest.main()