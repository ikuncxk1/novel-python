"""novel_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from novel.views import book
from novel.views.book import BookRecommendationListView, BookInfoDetailView, BookVisitView
from novel.views.chapter import LastChapterView
from novel.views.comment import NewestCommentsView
from novel.views.home import LatestNewsList, HomeBooksDetailView, BookVisitsView, NewBooksView, BookUpdatesView, \
    FriendLinksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/front/news/latest_list', LatestNewsList.as_view(), name='latest_news_list'),
    path('api/front/home/books', HomeBooksDetailView.as_view(), name='home_books'),
    path('api/front/book/visit_rank', BookVisitsView.as_view(), name='book_visits'),
    path('api/front/book/newest_rank', NewBooksView.as_view(), name='new_books'),
    path('api/front/book/update_rank', BookUpdatesView.as_view(), name='book_updates'),
    path('api/front/home/friend_Link/list', FriendLinksView.as_view(), name='home_links'),
    path('api/front/book/category/list', book.category_list, name='category_list'),
    path('api/front/search/books', book.book_search, name='book_search'),
    # path('api/front/book/rec_list', book.book_detail, name='book_detail'),
    path('api/front/book/comment/newest_list', NewestCommentsView.as_view(), name='newest_comments'),
    path('api/front/book/last_chapter/about', LastChapterView.as_view(), name='last_chapter'),
    path('api/front/book/rec_list', BookRecommendationListView.as_view(), name='book_rec_list'),
    path('api/front/book/<int:book_id>', BookInfoDetailView.as_view(), name='book_detail'),
    path('api/front/book/visit', BookVisitView.as_view(), name='book_visit'),
]
