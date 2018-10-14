import os
import pickle as pkl

class FileWriter:
    
    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(path):
            self._path = path
            self._file = None
    
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, new_path):
        if self._check_path(new_path):
            self._path = new_path
    
    @path.getter
    def path(self):
        return self._path
    
    @path.deleter
    def path(self):
        del self._path
        
    def _check_path(self, path):
        directory = os.path.dirname(path)
        return os.path.isdir(directory)
    
    def print_file(self):
        with open(self.path, 'r') as f:
            print(f.read())
    
    def write(self, some_string):
        if self._file is not None:
            self._file.write(some_string)
    
    def __enter__(self):
        self._file = open(self.path, 'a')
        return self
    
    def __exit__(self, type, value, traceback):
        self._file.close()
        self._file = None
    
    def save_yourself(self, file_name):
        if self._check_path(file_name):
            with open(file_name, 'wb') as f:
                pkl.dump(self, f)
    
    @classmethod
    def load_file_writer(cls, pickle_file):
        if cls._check_path(cls, pickle_file):
            with open(pickle_file, 'rb') as f:
                return pkl.load(f)