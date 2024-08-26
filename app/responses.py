""" Response Modules """


class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseFailure:
    def __init__(self, type_, message: str) -> None:
        self.type = type_
        self.message = message

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def Value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    """Response Success"""

    def __init__(self, value=None, data=None) -> None:
        self.type = ResponseTypes.SUCCESS
        self.value = value
        self.data = data

    def __bool__(self):
        return True


def build_response_from_invalid_request(invalid_request):
    message = "\n".join(["{}: {}".format(err["parameter"], err["message"]) for err in invalid_request.errors])

    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)
