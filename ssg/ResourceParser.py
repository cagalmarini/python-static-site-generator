
class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path : Path, source : Path, dest : Path):
        self.copy(path, source, dest)
