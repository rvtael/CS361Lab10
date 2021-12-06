import unittest

from TAScheduler.User.User import User


class CreateLabTests(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "User", 6500921, 991, "North Weil St", "abc123", "administrator")
        self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                            "Apoorv Prasad")
        self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                            "Chuanbo Yang")

    def validLabTest(self):
        self.user.createLab("Data Structures & Algorithms Lab", "9:00AM - 9:50AM", "EMS280", "Tuesday, Thursday",
                            "Hossein Ghanbari")
        # should check data base size with 3
        # self.assertEqual()
        self.user.createLab("Discrete Math Lab", "9:00AM - 9:50AM", "EMS280", "Monday, Wednesday",
                            "Hossein Ghanbari")
        # should check data base size with 4
        # self.assertEqual()

    def LabExistsTest(self):
        with self.assertRaises(TypeError, msg="This lab already exists: Failed to create lab"):
            self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                                "Apoorv Prasad")
        with self.assertRaises(TypeError, msg="This lab already exists: Failed to create lab"):
            self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                                "Chuanbo Yang")

    def invalidLabTest(self):
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to create lab"):
            self.user.createLab(None, "9:00AM - 9:50AM", "EMS280", "Monday, Wednesday",
                                "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to create lab"):
            self.user.createLab("Discrete Math Lab", None, "EMS280", "Monday, Wednesday",
                                "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to create lab"):
            self.user.createLab("Discrete Math Lab", "9:00AM - 9:50AM", None, "Monday, Wednesday",
                                "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to create lab"):
            self.user.createLab("Data Structures & Algorithms Lab", "9:00AM - 9:50AM", "EMS280", None,
                                "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to create lab"):
            self.user.createLab("Data Structures & Algorithms Lab", "9:00AM - 9:50AM", "EMS280", "Tuesday, Thursday",
                                None)


class EditLabTests(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "User", 6500921, 991, "North Weil St", "abc123", "administrator")
        self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                            "Apoorv Prasad")
        self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                            "Chuanbo Yang")

    def validEditLab(self):
        self.user.editLab("System Programming Lab", "9:00AM - 10:50AM", "EMS280", "Tuesday, Thursday",
                          "Chuanbo Yang")
        # should check if course is edited in the database
        # should check if it affected size
        self.user.editLab("Software Engineering Lab", "11:00AM - 11:50AM", "EMS180", "Wednesday, Friday",
                          "Chuanbo Yang")

    def invalidEditLab(self):
        with self.assertRaises(TypeError, msg="This lab does not exist: Failed to edit lab"):
            self.user.editLab("Discrete Math Lab", "11:00AM - 11:50AM", "EMS180", "Wednesday, Friday",
                              "Chuanbo Yang")
        with self.assertRaises(TypeError, msg="This lab does not exist: Failed to edit lab"):
            self.user.editLab("Data Structures & Algorithms Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                              "Apoorv Prasad")
        # should check if it affected size

    def valueErrorsEditLab(self):
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to edit lab"):
            self.user.editLab(None, "9:00AM - 9:50AM", "EMS280", "Monday, Wednesday",
                              "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to edit lab"):
            self.user.editLab("Discrete Math Lab", None, "EMS280", "Monday, Wednesday",
                              "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to edit lab"):
            self.user.editLab("Discrete Math Lab", "9:00AM - 9:50AM", None, "Monday, Wednesday",
                              "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to edit lab"):
            self.user.editLab("Data Structures & Algorithms Lab", "9:00AM - 9:50AM", "EMS280", None,
                              "Hossein Ghanbari")
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to edit lab"):
            self.user.editLab("Data Structures & Algorithms Lab", "9:00AM - 9:50AM", "EMS280", "Tuesday, Thursday",
                              None)


class DeleteLabTests(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "User", 6500921, 991, "North Weil St", "abc123", "administrator")
        self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                            "Apoorv Prasad")
        self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                            "Chuanbo Yang")

    def validDeleteLab(self):
        self.user.deleteLab("System Programming Lab")
        # check size to see if database is deleted
        # checks to see if database has the course deleted

    def invalidDeleteLab(self):
        with self.assertRaises(TypeError, msg="This lab does not exist: Failed to delete lab"):
            self.user.deleteLab("Data Structures & Algorithms Lab")
        with self.assertRaises(TypeError, msg="This lab does not exist: Failed to delete lab"):
            self.user.deleteLab("Discrete Math Lab")

    def valueErrorsDeleteLab(self):
        with self.assertRaises(ValueError, msg="The inputs are invalid: Failed to delete lab"):
            self.user.deleteLab(None)


class PopulateSearchLabTests(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "User", 6500921, 991, "North Weil St", "abc123", "administrator")
        self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                            "Apoorv Prasad")
        self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                            "Chuanbo Yang")

    def validPopulateSearchLabTests(self):
        K = 4
        # ???

    def invalidPopulateSearchLabTests(self):
        with self.assertRaises(TypeError, msg="Search Prompt is not valid: Failed to Populate Search Lab"):
            self.user.populateSearchLab(None)


class DisplayAllLabs(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "User", 6500921, 991, "North Weil St", "abc123", "administrator")
        self.user.createLab("Software Engineering Lab", "10:00AM - 10:50AM", "EMS180", "Monday, Wednesday",
                            "Apoorv Prasad")
        self.user.createLab("System Programming Lab", "10:00AM - 10:50AM", "EMS180", "Tuesday, Thursday",
                            "Chuanbo Yang")
        self.user2 = User("2", "User2", 6500922, 992, "South Weil St", "123abc", "administrator")

    def validDisplayAllLabsTests(self):
        self.user.displayAllLabs()
        # should check if database doesn't change

    def invalidDisplayAllCourseTests(self):
        with self.assertRaises(TypeError, msg="Their are no labs to display: Failed to display labs"):
            self.user2.displayAllLabs()
