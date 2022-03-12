from django.urls import path
from graphene_django.views import GraphQLView

from call_for_volunteers.schema_graphql import schema

urlpatterns = [
    # GraphQL
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
