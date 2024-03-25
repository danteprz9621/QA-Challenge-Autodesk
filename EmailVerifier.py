class EmailVerifier:

    def is_valid_email(self, email):
        """
    Function checks if an email is valid based on the following criteria:

    - The prefix name can contain letters (upper or lower case), digits, underscore (_), period(.), and/or dash(-).
    - The prefix name must start with a letter.
    - The domain must be '@codechallenge.com'.

    Args:
        email: The email address to be validated.

    Returns:
        True if the email is valid, False otherwise.
    """

        try:
            # Check if email is a string and not empty
            if not isinstance(email, str) or not email:
                return False

            # Check if email has the minimum value to be considered valid
            if len(email) < len("@codechallenge.com") + 1:
                return False

            # Split the email at the "@" symbol
            parts = email.split("@")

            # Check if there are two parts after the split
            if len(parts) != 2:
                return False

            # Validate the prefix name
            prefix = parts[0]
            if not prefix or not prefix[0].isalpha():
                return False

            # Validate whether any of the characters in string is not alphanumeric
            # or not a dash, underscore or period character
            for char in prefix:
                if not char.isalnum() and char not in "-_.":
                    return False

            # Validate the domain
            domain = parts[1]
            if domain != "codechallenge.com":
                return False

            return True
        except (AttributeError, ValueError):
            # Handle potential exceptions like splitting a non-string or empty input
            return False
