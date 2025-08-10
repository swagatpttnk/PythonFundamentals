from com.sppt.errorhandling.CustomException import MyCustomException


class BasicExceptionHandling:
    def __init__(self):
        pass

    def raise_exception_implicitly(self):
        raise MyCustomException("My Custom exception", 500)


    def demo_exception_handling(self):
        file_path = "my_data.txt"
        file = None  # Initialize file handle

        try:
            file = open(file_path, "r")
            content = file.read()
            print("File content:")
            print(content)
            self.raise_exception_implicitly()

        except FileNotFoundError as e:
            print(f"Error: File '{file_path}' not found. Error message:{e}")
        except MyCustomException as e:
            print(f"MyCustomException - Error message:{e}")
            raise #<-- If no exception type is provided , Python raises the above exception
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        else:
            print(f"ELSE block executed => no exception in the TRY block...")
        finally:
            # This block always executes
            if file:  # Check if the file was actually opened
                file.close()
                print("File closed.")