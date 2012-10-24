def monkeypatch(cls):
    """
    Dynamically add a method to an existing class::

        from <somewhere> import <someclass>

        @monkeypatch(<someclass>)
        def <newmethod>(self, args):
            return <whatever>
    """
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator
