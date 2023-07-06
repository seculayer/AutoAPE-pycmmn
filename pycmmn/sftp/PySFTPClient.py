# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import stat
import paramiko
import os

from pycmmn.crypto.AES256 import AES256
from pycmmn.exceptions.PySFTPAuthException import PySFTPAuthException
from pycmmn.utils.FileUtils import FileUtils


class PySFTPClient(object):
    # class : PySFTPClient
    def __init__(self, host: str, port: int, username: str, password: str):
        try:
            self.transport = paramiko.Transport((host, port))
            self.transport.connect(username=AES256().decrypt(username), password=AES256().decrypt(password))
            self.sftp: paramiko.SFTPClient = paramiko.SFTPClient.from_transport(self.transport)
        except paramiko.ssh_exception.AuthenticationException:
            info_dict = {
                "host": host,
                "port": port,
                "username": username,
                "password": password
            }
            raise PySFTPAuthException(info_dict)

    def open(self, filename, option="r",) -> paramiko.SFTPFile:
        return self.sftp.open(filename, option)

    def close(self):
        self.sftp.close()
        self.transport.close()

    def rename(self, src, dst):
        self.sftp.rename(src, dst)

    def is_exist(self, filename) -> bool:
        try:
            self.sftp.stat(filename)
            return True
        except FileNotFoundError:
            return False

    def get_file_list(self, dir_path) -> list:
        return self.sftp.listdir(dir_path)

    def delete_file(self, file_path):
        self.sftp.remove(file_path)

    def mkdir(self, dir_path):
        if not self.is_exist(dir_path):
            self.sftp.mkdir(dir_path)

    def is_dir(self, remote_path) -> bool:
        fileattr = self.sftp.lstat(remote_path)
        is_dir = False

        if stat.S_ISDIR(fileattr.st_mode):
            is_dir = True
        elif stat.S_ISREG(fileattr.st_mode):
            is_dir = False

        return is_dir

    def scp_to_storage(self, local_path, remote_path):
        self._scp_send_recursive(local_path, remote_path)

    def _scp_send_recursive(self, local_path, remote_path):
        is_dir = os.path.isdir(local_path)
        if local_path.__contains__('/'):
            curr_dir_name = local_path.rsplit('/', 1)[1]
        else:
            curr_dir_name = local_path

        if is_dir:
            self.mkdir(f"{remote_path}/{curr_dir_name}")
            for file_name in os.listdir(local_path):
                self._scp_send_recursive(f"{local_path}/{file_name}", f"{remote_path}/{curr_dir_name}")
        else:
            self.sftp.put(local_path, f"{remote_path}/{curr_dir_name}")

    def scp_from_storage(self, remote_path, local_path):
        self._scp_receive_recursive(remote_path, local_path)

    def _scp_receive_recursive(self, remote_path, local_path):
        is_dir = self.is_dir(remote_path)
        curr_dir_name = remote_path.rsplit('/', 1)[1]

        if is_dir:
            FileUtils.mkdir(f"{local_path}/{curr_dir_name}")
            for file_name in self.sftp.listdir(remote_path):
                self._scp_receive_recursive(f"{remote_path}/{file_name}", f"{local_path}/{curr_dir_name}")
        else:
            self.sftp.get(remote_path, f"{local_path}/{curr_dir_name}")


if __name__ == '__main__':
    sftp_client = PySFTPClient("localhost", 22, "Kmw/y3YWiiO7gJ/zqMvCuw==", "jTf6XrqcYX1SAhv9JUPq+w==")
    with sftp_client.open("/home/seculayer/temp.tmp", "w") as f:
        f.write("test.1" + "\n")

    with sftp_client.open("/home/seculayer/temp.tmp", "r") as f:
        for line in f.readlines():
            print(line)
    sftp_client.close()
