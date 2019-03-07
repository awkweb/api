from django.db import DEFAULT_DB_ALIAS, connections
from django.db.migrations.executor import MigrationExecutor
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response


@api_view()
def index(request):
    return Response(status=HTTP_204_NO_CONTENT)


@api_view()
def health_check(request):
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
    plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
    status = 503 if plan else 200
    return Response(status=status)

