import random

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    #success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        if form.is_valid():
            code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            self.object.verification_code = code
            self.object.is_active = False
            self.object.save()
            send_mail(
                'email verification',
                f'Your code - {code}',
                settings.EMAIL_HOST_USER,
                [self.object.email]
            )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:verification', kwargs={'email': self.object.email})


def verify_email(request, email):
    """Контроллер верификации почты"""
    if request.method == 'POST':
        code_to_check = request.POST.get('verification_code')
        user = User.objects.get(email=email)
        if user.verification_code == code_to_check:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))
        else:
            raise ValidationError(f'You have used the wrong code!')
    else:
        context = {'page_title': 'Email verification'}
        return render(request, 'users/verify_email.html', context)


class ProfileView(UpdateView):
    """Контроллер для просмотра профиля пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
