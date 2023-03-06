from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Comment, Ad
from ads.permissions import IsAdAuthorOrStaff
from ads.serializers import CommentSerializer, AdSerializer, AdDetailSerializer, CommentCreateSerializer

from django_filters.rest_framework import DjangoFilterBackend
from filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class CommentPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)  # Подключаем библиотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр
    queryset = Ad.objects.order_by("-created_at")
    pagination_class = AdPagination
    default_serializer = AdSerializer
    serializer_classes = {
        'retrieve': AdDetailSerializer,
        'list': AdSerializer
    }

    default_permission = [AllowAny()]
    permission_list = {"retrieve": [AllowAny()],
                       "create": [IsAuthenticated(), IsAdAuthorOrStaff(), ],
                       "update": [IsAdAuthorOrStaff(), ],
                       "partial_update": [IsAdAuthorOrStaff(), ],
                       "destroy": [IsAdAuthorOrStaff(), ],
                       }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permission_list.get(self.action, self.default_permission)

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data["author"] = request.user.pk
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    default_serializer = CommentSerializer
    pagination_class = CommentPagination

    serializer_classes = {
        'retrieve': CommentSerializer,
        'list': CommentSerializer,
        'create': CommentCreateSerializer
    }

    default_permission = [AllowAny()]
    permission_list = {"retrieve": [AllowAny()],
                       "create": [IsAuthenticated(), IsAdAuthorOrStaff(), ],
                       "update": [IsAdAuthorOrStaff(), ],
                       "partial_update": [IsAdAuthorOrStaff(), ],
                       "destroy": [IsAdAuthorOrStaff(), ],
                       }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_permissions(self):
        return self.permission_list.get(self.action, self.default_permission)

    def get_queryset(self):
        return Comment.objects.prefetch_related("author").filter(
            ad=self.kwargs["ad_pk"]
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, ad_id=self.kwargs.get("ad_pk"))
