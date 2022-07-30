"""
Enabler
-------
An efficient way to enable python pipeline.
"""


class Enabler:
    """"Enabler Class"""

    def __init__(
            self,
            name: str,
    ) -> None:
        """"
            Init the Enable with the variables.
        """
        self.name = name

    def _get_name(self):
        """ Return the name of the enabler"""
        return self.name
