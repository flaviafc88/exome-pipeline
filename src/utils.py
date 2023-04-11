import glob
import os

class Utils(object):
    @staticmethod
    def print(param1):
        print(param1)

    @staticmethod
    def listFiles(path, pattern):
        if (len(pattern) > 0) :
            path = path + '/' + pattern
        return glob.glob(path)

    @staticmethod
    def folderExists(path):
        return os.path.exists(path) and os.path.isdir(path)