from django.views.generic import ListView
from users.models.accounts import Account


class IndexView(ListView):
    template_name = 'index.html'
    model = Account
    context_object_name = 'user_obj'