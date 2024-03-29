from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommentsConfig(AppConfig):
    name = "hispace.comments"
    verbose_name = _("Comments")

    def ready(self):
        try:
            import hispace.comments.signals  # noqa F401
        except ImportError:
            pass
