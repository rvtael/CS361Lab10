from TAScheduler.models import UserProfile

class Instructor:
    def __init__(self, id, name, contact):
        self.id = id
        pass

    def assign_course(self, TA_ref, section_id):
        # 1. filter out all the TAs
        filtered_TA = UserProfile.objects.filter(userType='TA', userName='toy_ta')
        Course.objects.update(section=section_id, )
        pass

    def retrieve_all_TAs(self):
        passs