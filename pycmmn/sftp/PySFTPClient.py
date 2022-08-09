# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import paramiko
from scp import SCPClient, SCPException
from pycmmn.crypto.AES256 import AES256
from pycmmn.exceptions.PySFTPAuthException import PySFTPAuthException


class PySFTPClient(object):
    # class : PySFTPClient
    def __init__(self, host: str, port: int, username: str, password: str):
        try:
            self.transport = paramiko.Transport((host, port))
            self.transport.connect(username=AES256().decrypt(username), password=AES256().decrypt(password))
            self.sftp: paramiko.SFTPClient = paramiko.SFTPClient.from_transport(self.transport)
        except paramiko.ssh_exception.AuthenticationException:
            raise PySFTPAuthException

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
        self.sftp.mkdir(dir_path)

    def scp_to_storage(self, local_path, remote_path):
        try:
            with SCPClient(self.transport) as scp:
                scp.put(local_path, remote_path, recursive=True, preserve_times=True)
        except SCPException:
            raise SCPException

    def scp_from_storage(self, remote_path, local_path):
        try:
            with SCPClient(self.transport) as scp:
                scp.get(remote_path, local_path, recursive=True)
        except SCPException:
            raise SCPException


if __name__ == '__main__':
    sftp_client = PySFTPClient("localhost", 22, "Kmw/y3YWiiO7gJ/zqMvCuw==", "jTf6XrqcYX1SAhv9JUPq+w==")
    with sftp_client.open("/home/seculayer/temp.tmp", "w") as f:
        f.write("test.1" + "\n")

    with sftp_client.open("/home/seculayer/temp.tmp", "r") as f:
        for line in f.readlines():
            print(line)
    sftp_client.close()
