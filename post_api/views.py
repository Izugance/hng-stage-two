import operator
from enum import Enum

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import ArithmeticSerializer
from .models import ArithmeticQueryModel


class OperationEnum(Enum):
    """An enumeration over acceptable operation types."""

    addition = operator.add
    add = operator.add
    sum = operator.add
    plus = operator.add
    minus = operator.sub
    subtract = operator.sub
    subtraction = operator.sub
    sub = operator.sub
    multiply = operator.mul
    mul = operator.mul
    times = operator.mul


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def arithmetic_post_view(request, *args, **kwargs):
    """Parse the json content of the request's post and return
    the result of the arithmetic operation in a specified format
    """
    if request.method == "GET":
        pass
    elif request.method == "POST":
            serializer = ArithmeticSerializer(data=request.data)
            return JsonResponse(request.data)
            if serializer.is_valid():
                serializer.save()
                received_data = serializer.validated_data
                operation_type = received_data["operation_type"].lower().strip()
                x = received_data["x"]
                y = received_data["y"]
                try:
                    input_operator = OperationEnum[operation_type].value
                except Exception:
                    return Response({"error": "Unknown operation"})
                else:
                    result = input_operator(x, y)
                    response_data = {
                        "slackUsername": "@izugance",
                        "operation_type": operation_type,
                        "result": result,
                    }
                    return Response(response_data)
