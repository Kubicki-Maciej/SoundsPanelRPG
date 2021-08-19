import os
import settings as s


class SearchFile:

    def __init__(self):
        self.files = os.listdir()


class FileMusicList(list):

    def search(self):
        """search for file name music"""
        files_list = []
        for file in self:
            for each_type in s.types:
                if each_type in file.file_name:
                    self.files_list.append(file)
        return files_list


class File:

    all_files = FileMusicList()

    def __init__(self, filename):
        self.file_name = filename
        self.type = self.get_file_type()
        self.category = None

        File.all_files.append(self)

    @staticmethod
    def files_in_music_folders():
        return os.listdir(s.music_path)

    def get_file_type(self):
        pass


class Files(File):
    pass