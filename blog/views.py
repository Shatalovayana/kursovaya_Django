from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog
from blog.services import get_cached_blogs


class BlogCreateView(CreateView):
    """Контроллер для создания блога"""
    model = Blog
    fields = ('title', 'body', 'image', 'created_at', 'views_count',)
    success_url = reverse_lazy('blog:list')


class BlogUpdateView(UpdateView):
    """Контроллер для редактирования блога"""
    model = Blog
    fields = ('title', 'body', 'image', 'views_count',)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    """Контроллер для просмотра списка блогов"""
    model = Blog
    extra_content = {"title": "Blog"}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = get_cached_blogs()
        return context_data


class BlogDetailView(DetailView):
    """Контроллер для просмотра отдельного блога"""
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    """Контроллер для удаления блога"""
    model = Blog
    success_url = reverse_lazy('blog:list')

