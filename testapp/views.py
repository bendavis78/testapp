from django.views.generic import edit, list
from testapp import models

class PersonCreate(edit.CreateView):
    success_url = '/'
    def get_initial(self):
        initial = super(PersonCreate, self).get_initial()
        initial['first_name'] = 'initial'
        initial['last_name'] = 'data'
        return initial

class PersonUpdate(edit.UpdateView):
    success_url = '/'

opts = {
    'model': models.Person
}

index = list.ListView.as_view(**opts)
create = PersonCreate.as_view(**opts)
update = PersonUpdate.as_view(**opts)
