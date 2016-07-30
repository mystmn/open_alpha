import os


class MainController(object):
    def __init__(self, root_path, seek_name):
        self.seek = seek_name
        self.paths = [
            root_path,
            '\models'
            '\controllers'
            '\helpers'
            'database.db'
        ]

    def model_connection(self):

        integity
        if self.confirm_path():
            print("continue")
        else:
            print("path not found :: {}".format(self.paths[0] + self.paths[2] + self.seek))

        filename = self.var.replace(".py", "")
        self.confirm_path()
        print(filename)

    def secure_database_connection(self):
        pass

    def confirm_path(self):
        if os.path.isdir()

if __name__ == '__main__':
    MainController().model_connection()
