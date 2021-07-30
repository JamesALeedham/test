class g:
    """
    This is a base class.
    """
    def __init__(self, arg1: int, arg2: str):
        """
        :param arg1: Pass a :data:`~mytoolbox.mymodule1.myTypeAlias` in first.
        :param arg2: Pass a string in second.
        """
        self.arg = arg1

    def myMethod1(self, arg: int) -> str:
        """
        This is the first public method.
        :param arg: Pass a :data:`~mytoolbox.mymodule1.myTypeVar` in.
        :return: Get one of these out.
        """
        pass
