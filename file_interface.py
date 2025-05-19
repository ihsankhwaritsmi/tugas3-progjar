import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir("files/")

    def list(self, params=[]):
        try:
            filelist = glob("*.*")
            return dict(status="OK", data=filelist)
        except Exception as e:
            return dict(status="ERROR", data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if filename == "":
                return None
            fp = open(f"{filename}", "rb")
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status="OK", data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status="ERROR", data=str(e))

    def upload(self, params=[], max_workers=2):
        try:
            if len(params) < 2:
                return dict(status="ERROR", data="Parameter kurang untuk upload")
            filename = params[0]
            file_base64 = params[1]
            # decode isi file dari base64 ke bytes
            file_bytes = base64.b64decode(file_base64)
            # tulis file ke disk
            with open(filename, "wb") as f:
                f.write(file_bytes)
            return dict(status="OK", data=f"File {filename} berhasil diupload")
        except Exception as e:
            return dict(status="ERROR", data=str(e))

    def delete(self, params=[]):
        try:
            if len(params) < 1:
                return dict(status="ERROR", data="Nama file belum diberikan")

            filename = params[0]
            if not os.path.exists(filename):
                return dict(status="ERROR", data=f"File {filename} tidak ditemukan")

            os.remove(filename)
            return dict(status="OK", data=f"File {filename} berhasil dihapus")
        except Exception as e:
            return dict(status="ERROR", data=str(e))


if __name__ == "__main__":
    f = FileInterface()
    print(f.list())
    print(f.get(["pokijan.jpg"]))
