from py_ui import profile_teacher, profile_children

from profile import ProfileTab
from tasks import TasksTab, ManageTasksTab
from create_class import CreateClassTab


# unification of children profile and tasks design
class ChildrenApp(ProfileTab, TasksTab, profile_children.Ui_Form):
    def __init__(self):
        super().__init__(self)
        TasksTab().__init__(self)


# unification of teacher profile and tasks design
class TeacherApp(ProfileTab, ManageTasksTab, CreateClassTab):
    def __init__(self):
        super().__init__(self)
        ManageTasksTab(self).__init__(self)
        CreateClassTab(self).__init__(self)
