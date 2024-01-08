# user_interface.py

class UserInterface:
    @staticmethod
    def get_user_input():
        """
        Get user input for the URL.
        :return: The user-entered URL.
        """
        url = input("Enter the URL: ")
        return url.strip()

    @staticmethod
    def display_result(result):
        """
        Display the result to the user.
        :param result: The result message to be displayed.
        """
        print(result)

if __name__ == "__main__":
    # Example usage in case user_interface.py is run directly
    ui = UserInterface()
    url_input = ui.get_user_input()
    ui.display_result(f"User entered URL: {url_input}")
