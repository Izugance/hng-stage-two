import operator
from enum import Enum

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
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


@api_view(["POST"])
def arithmetic_post_view(request, *args, **kwargs):
    """Parse the json content of the request's post and return
    the result of the arithmetic operation in a specified format
    """
    if request.method == "POST":
        return request.body
        serializer = ArithmeticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            received_data = serializer.data
            operation_type = received_data["operation_type"].lower().strip()
            x = received_data["x"]
            y = received_data["y"]
            try:
                input_operator = OperationEnum[operation_type].value
            except Exception:
                return Response("Unknown operation")
            else:
                result = input_operator(x, y)
                response_data = {
                    "slackUsername": "@izugance",
                    "operation_type": operation_type,
                    "result": result,
                }
                return Response(response_data)
