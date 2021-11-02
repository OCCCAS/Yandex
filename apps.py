from PyQt5.QtWidgets import QWidget

from profile import Profile
from tasks import Tasks, ManageTasks
import py_ui.profile_teacher
import py_ui.profile_children


# unification of children profile and tasks design
class ChildrenApp(Profile, Tasks, py_ui.profile_children.Ui_Form):
    def __init__(self):
        Tasks.__init__(self)
        Profile.__init__(self)


# unification of teacher profile and tasks design
class TeacherApp(Profile, ManageTasks, py_ui.profile_teacher.Ui_Form):
    def __init__(self):
        ManageTasks.__init__(self)
        Profile.__init__(self)

