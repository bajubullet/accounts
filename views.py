from django.views.generic.edit import FormView

from accounts.forms import UserCreateForm


class SignupView(FormView):
    '''
    Renders signup form.
    '''
    form_class = UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        '''
        Create user, login and redirect.
        '''
        user = form.save()
        return super(SignupView, self).form_valid()