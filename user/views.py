from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm, PassChangeForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, get_urlconf
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import Profile 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            # messages.success(
            #    request, 'تهانينا {} لقد تمت عملية التسجيل بنجاح.'.format(username))
            messages.success(
                request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {
        'title': 'التسجيل',
        'form': form,
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', args=[request.user.id])
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')

    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
    })

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج'
    })

class profile(DetailView):
    model = Profile
    template_name = 'user/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        posts = Post.objects.filter(author=self.kwargs['pk'])
        post_list = Post.objects.filter(author=self.kwargs['pk'])
        paginator = Paginator(post_list, 10)
        # page =  request.GET.get('page')
        page =  get_urlconf()
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_page)
        context = super(profile, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])

        context['page_user'] = page_user
        context['posts'] = posts
        context['post_list'] = post_list
        context['page'] = page
        return context

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)


class PasswordsChange(PasswordChangeView):
    template_name = 'user/change-pass.html'
    form_class = PassChangeForm
    success_url = reverse_lazy('pass_succ')

@login_required(login_url='login')
def pass_succ(request):
    return render(request, 'user/pass_succ.html', {})    