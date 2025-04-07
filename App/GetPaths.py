import os

class GetPaths:
    def __init__(self):
        self.__sourceDirectory: str = "./Source"
        self.__translationDirectory: str = "./Translation"
        self.checkDirectories()

    # creates a dict of paths to all files in *self.__sourceDirectory*
    def getPaths(self) -> dict[str, str]:
        try:
            paths: dict[str, str] = {}
            # root: current folder; dirs: all recursive folders; files: only filenames
            for root, dirs, files in os.walk(self.__sourceDirectory):
                # iterates the list of filenames
                for file in files:
                    # makes a complete path to filename
                    sourcePath: str = os.path.join(root, file)
                    paths[sourcePath] = sourcePath.replace(self.__sourceDirectory, self.__translationDirectory)
            return paths
        except Exception as e:
            print(f"Error occurred: {e}")

    # exist if folders not exits
    def checkDirectories(self):
        try:
            if not os.path.exists(self.__sourceDirectory):
                raise f"Directory *{self.__sourceDirectory}* not found"
            elif not os.path.exists(self.__translationDirectory):
                raise f"Directory *{self.__translationDirectory}* not found"
        except Exception as e:
            print(f"Error occurred: {e}")
            exit()