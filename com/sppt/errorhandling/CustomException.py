class MyCustomException(RuntimeError):
    """
     This is the documentation about the error MyCustomException , is thrown when developer xxx event happens.
    """

    # Now lets define the error
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

