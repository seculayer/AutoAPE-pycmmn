# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.
import json
from typing import List, Dict
import numpy as np

from pycmmn.Singleton import Singleton
from pycmmn.sftp.PySFTPClient import PySFTPClient
from pycmmn.utils.ImageUtils import ImageUtils
from pycmmn.logger.MPLogger import MPLogger
from pycmmn.Constants import Constants


class SFTPClientManager(object, metaclass=Singleton):
    # class : SFTPClientManager
    def __init__(self, service: str, username: str, password: str, logger: MPLogger.getLogger):
        self.logger = logger
        self.service: List[str] = service.split(":")
        self.username = username
        self.password = password

        self.sftp_client = PySFTPClient(self.service[0], int(self.service[1]),
                                        self.username, self.password)

        self.logger.info("initialized service - [{}] SFTP Client Initialized.".format(service))

    def get_client(self) -> PySFTPClient:
        return self.sftp_client

    def rename(self, src, dst) -> None:
        self.sftp_client.rename(src, dst)

    def close(self) -> None:
        self.sftp_client.close()

    def load_json_data(self, filename):
        json_data = None
        f = None
        try:
            f = self.get_client().open(filename, "r")
            json_data = json.loads(f.read())
        except Exception as e:
            self.logger.error(e, exc_info=True)
            self.logger.error(f"file path : {filename}")
        finally:
            f.close()
        return json_data

    def load_json_oneline(self, filename: str, dataset_format: str):
        f = self.get_client().open(filename, "r")
        data = None
        while True:
            try:
                data = f.readline()
                if data is None or data == "":
                    yield "#file_end#"
                    break
                else:
                    if dataset_format == Constants.DATASET_FORMAT_TEXT:
                        yield json.loads(data)
                    elif dataset_format == Constants.DATASET_FORMAT_IMAGE:
                        file_path = filename.rsplit('/', 1)[0]
                        json_data: Dict = json.loads(data)
                        img_byte: bytes = self._read_image_binary(file_path, json_data)
                        img_data: np.array = ImageUtils.load(img_byte)
                        img_data = img_data.tolist()

                        json_data["image"] = img_data
                        yield json_data
            except Exception as e:
                self.logger.error(data)
                self.logger.error(e, exc_info=True)
                break

        f.close()

    def _read_image_binary(self, file_path: str, annotation_data: Dict) -> bytes:
        filename = annotation_data.get("file_conv_nm")
        img_f = self.sftp_client.open("{}/{}".format(file_path, filename, "rb"))
        img_array = img_f.read()
        img_f.close()
        return img_array

    def mkdir(self, dir_path):
        return self.sftp_client.mkdir(dir_path)

    def is_exist(self, filename) -> bool:
        return self.sftp_client.is_exist(filename)

    def scp_to_storage(self, local_path, remote_path):
        self.sftp_client.scp_to_storage(local_path, remote_path)

    def scp_from_storage(self, remote_path, local_path):
        self.sftp_client.scp_from_storage(remote_path, local_path)


if __name__ == '__main__':
    sm = SFTPClientManager("10.1.35.118:22", "Kmw/y3YWiiO7gJ/zqMvCuw==", "jTf6XrqcYX1SAhv9JUPq+w==")
    gee = sm.load_json_oneline("/eyeCloudAI/data/processing/ape/division/99429867778487988_0.done")

    while True:
        print(next(gee))
