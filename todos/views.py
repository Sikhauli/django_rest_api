from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.serializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from todos.models import Todo 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters

class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete', 'desc' ]
    search_fields = ['id', 'title', 'is_complete', 'desc' ]
    ordering_fields = ['id', 'title', 'is_complete', 'desc' ]


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = TodoSerializer
    permission_classes=[IsAuthenticated]
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

