import os


# Reminder to add validation and docstring

class LoadFilenames:
    def __init__(self, path: str = None):
        self.path = path or "c:/podcasts/"
        self.filenames = self.get_list_of_filenames(self.path)


    def get_list_of_filenames(self, path: str):
        list_of_filenames = []
        for filename in os.listdir(path):
            list_of_filenames.append(filename)

        return  list_of_filenames

