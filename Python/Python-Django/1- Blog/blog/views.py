from django.shortcuts import render, get_object_or_404, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from .models import Post, Comment
from django.core.mail import send_mail
from taggit.models import Tag, TaggedItem
from django.db.models import Count


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        tagged_items = TaggedItem.objects.filter(tag=tag)
        post_ids = [ti.content_object.id for ti in tagged_items]
        object_list = object_list.filter(id__in=post_ids)

    
    paginator = Paginator(object_list, 3) # três postagens em cada página
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página
        posts = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo,
        # exibe a útima página de resultados
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts': posts, 'tag':tag})
    
    


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # Lista dos comentários ativos para esta postagem
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # Um comentário foi postado
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Cria o objeto Comment, mas não o
            # salva ainda no banco de dados
            new_comment = comment_form.save(commit=False)
            # Atribui a postagem atual ao comentário
            new_comment.post = post
            # Salva o comentário no banco de dados
            new_comment.save()
    else:
        comment_form = CommentForm()
    # Artigos semelhantes
    similar_posts = self.object.tags.similar_objects
    return render(request, 'blog/post/detail.html', {'post': post,
    'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form,
    'similar_posts': similar_posts})
    
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    #  Obtém a postagem com base no id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        #  Formulário foi submetido
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #  Campos do formulário passaram pela validação
            cd = form.cleaned_data
            #  ... envia o email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url} \n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    
    else:          
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})