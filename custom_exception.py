class UnknownTimeZoneError(KeyError):

    def __init__(self, zone):
        self.zone = zone

    def __str__(self):
        return "There is no time zone called {!r}".format(self.zone)

raise UnknownTimeZoneError('Istanbul')
