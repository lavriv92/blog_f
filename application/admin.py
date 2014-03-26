from flask.ext.admin.contrib.sqla import ModelView

from models import Category, Post


class CategoryView(ModelView):
    form_excluded_columns = ('created', 'posts', )

    def __init__(self, session, **kwargs):
        super(CategoryView, self).__init__(Category, session, **kwargs)


class PostView(ModelView):

    form_excluded_columns = ('created')
    column_filters = ('category', )

    def __init__(self, session, **kwargs):
        super(PostView, self).__init__(Post, session, **kwargs)
