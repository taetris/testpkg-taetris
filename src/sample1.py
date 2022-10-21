# Sample Header File

class TextTransform:
    def __init__(self):
        pass

    @staticmethod
    def t_lower(string: str):
        """
        Converts a string to lowercase
        """
        return string.lower()

    @staticmethod
    def t_upper(string: str):
        """
        Converts a string to uppercase
        """
        return string.upper()

    @staticmethod
    def t_title(string: str):
        """
        Converts a string to titlecase
        """
        return string.title()

    @staticmethod
    def t_kebab(string: str):
        """
        Converts a string to kebabcase
        """
        return string.replace(" ", "-").lower()

if __name__ == '__main__':
    print("Sample textTransform class loaded.")