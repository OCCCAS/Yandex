from profile import ChildrenProfile, TeacherProfile
from tasks import *


# unification of children profile and tasks design
class ChildrenApp(ChildrenProfile, Tasks, QWidget):
    def __init__(self):
        super().__init__()


# unification of teacher profile and tasks design
class TeacherApp(TeacherProfile, ManageTasks, QWidget):
    def __init__(self):
        super().__init__()


