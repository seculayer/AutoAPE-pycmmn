# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import requests as rq
import re
import json
import os
import psutil
import GPUtil
from typing import List, Union

from pycmmn.Common import Common
from pycmmn.Constants import Constants
from pycmmn.Singleton import Singleton
from pycmmn.logger.MPLogger import MPLogger


class RestManager(object, metaclass=Singleton):

    @staticmethod
    def get(url: str, logger: MPLogger.getLogger) -> str:
        response = rq.get(url)
        logger.debug("GET {}".format(url))

        return response.text

    @staticmethod
    def post(url: str, data: dict, logger: MPLogger.getLogger) -> rq.Response:
        response = rq.post(url, json=data)
        logger.debug("POST {}".format(url))
        logger.debug("POST DATA: {}".format(data))

        return response

    @staticmethod
    def get_cnvr_dict(rest_url_root: str, logger: MPLogger.getLogger) -> dict:
        url = rest_url_root + Common.REST_URL_DICT.get("cnvr_list", "")
        func_dict_list = json.loads(RestManager.get(url, logger))
        convert_dict = dict()

        re_exp = "\\[\\[@(.+)\\(\\)\\]\\]"
        p1 = re.compile(re_exp)

        for func_dict in func_dict_list:
            cvt_dict = dict()
            cvt_dict["class"] = func_dict["conv_func_cls"]
            function_nm = p1.match(func_dict["conv_func_tag"]).group(1)

            convert_dict[function_nm] = cvt_dict

        return convert_dict

    @staticmethod
    def get_status_cd(rest_url_root: str, logger: MPLogger.getLogger, job_type: str, job_key: str) -> str:
        if job_type == Constants.JOB_TYPE_LEARN:
            url = rest_url_root + Common.REST_URL_DICT.get("get_status_cd", "")
        else:  # job_type == Constants.JOB_TYPE_INFERENCE:
            url = rest_url_root + Common.REST_URL_DICT.get("get_infr_status_cd", "")
        hist_no = job_key.split("_")[-1]
        data = {
            "hist_no": hist_no
        }
        return RestManager.post(url, data, logger).text

    @staticmethod
    def get_project_id(rest_url_root: str, logger: MPLogger.getLogger, job_key: str) -> str:
        url = rest_url_root + Common.REST_URL_DICT.get("get_project_id", "")
        hist_no = job_key.split("_")[-1]
        return RestManager.get(f"{url}?hist_no={hist_no}", logger)

    @staticmethod
    def update_status_cd(rest_url_root: str, logger: MPLogger.getLogger, job_type: str, status: str, job_key: str, task_idx: str, msg: str) -> rq.Response:
        if job_type == Constants.JOB_TYPE_LEARN:
            url = rest_url_root + Common.REST_URL_DICT.get("learn_status_update", "")
        else:  # job_type == Constants.JOB_TYPE_INFERENCE:
            url = rest_url_root + Common.REST_URL_DICT.get("infr_status_update", "")
        hist_no = job_key.split("_")[-1]
        obj = {
            "sttus_cd": status,
            "hist_no": hist_no,
            "task_idx": task_idx,
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def update_eval_result(rest_url_root: str, logger: MPLogger.getLogger, job_key: str, task_idx: str, rst: Union[dict, list]) -> rq.Response:
        url = rest_url_root + Common.REST_URL_DICT.get("eval_result_update", "")
        hist_no = job_key.split("_")[-1]
        obj = {
            "hist_no": hist_no,
            "task_idx": task_idx,
            "result": rst
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def post_inference_result(rest_url_root: str, logger: MPLogger.getLogger, job_key: str, task_idx: str, global_sn: str, rst: List[Union[list, dict, int, str]]) -> rq.Response:
        url = rest_url_root + Common.REST_URL_DICT.get("inference_result_return", "")
        hist_no = job_key.split("_")[-1]
        obj = {
            "hist_no": hist_no,
            "task_idx": task_idx,
            "global_sn": global_sn,
            "result": rst
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def update_eps(rest_url_root: str, logger: MPLogger.getLogger, job_key: str, eps: float):
        url = rest_url_root + Common.REST_URL_DICT.get("eps_update", "")

        hist_no = job_key.split("_")[-1]
        obj = {
            "eps": eps,
            "hist_no": hist_no,
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def update_learn_result(rest_url_root: str, logger: MPLogger.getLogger, job_key: str, rst: list):
        url = rest_url_root + Common.REST_URL_DICT.get("learn_result_update", "")

        hist_no = job_key.split("_")[-1]
        obj = {
            "result": json.dumps(rst),
            "hist_no": hist_no,
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def update_time(rest_url_root: str, logger: MPLogger.getLogger, job_type: str, job_key: str, _type: str):
        if job_type == Constants.JOB_TYPE_LEARN:
            url = rest_url_root + Common.REST_URL_DICT.get("time_update", "")
        else:  # job_type == Constants.JOB_TYPE_INFEREN:
            url = rest_url_root + Common.REST_URL_DICT.get("infr_time_update", "")

        hist_no = job_key.split("_")[-1]
        obj = {
            "type": _type,
            "hist_no": hist_no
        }
        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def send_resource_usage(rest_url_root: str, logger: MPLogger.getLogger, job_key: str):
        url = rest_url_root + Common.REST_URL_DICT.get("model_resources", "")

        hist_no = job_key.split("_")[-1]
        pid = os.getpid()
        py = psutil.Process(pid)

        cpu_usage = os.popen(f"ps aux | grep {pid} | grep MLProcessingServer | grep -v grep | awk '{{print $3}}'").read()
        cpu_usage = cpu_usage.replace("\n", "")

        memory_dict = dict(psutil.virtual_memory()._asdict())
        memory_usage = round(py.memory_info()[0] / memory_dict['total'], 5)

        obj = {
            "learn_hist_no": hist_no,
            "memory": {"percent": memory_usage},
            "cpu": {"percent": cpu_usage},
            "gpu": {}
        }

        gpu_list = GPUtil.getGPUs()
        for gpu in gpu_list:
            obj["gpu"][gpu.id] = {}
            obj["gpu"][gpu.id]["memory"] = gpu.memoryUtil * 100
            obj["gpu"][gpu.id]["percent"] = gpu.load * 100
            obj["gpu"][gpu.id]["temperature"] = gpu.temperature

        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def send_inference_progress(rest_url_root: str, logger: MPLogger.getLogger, job_key: str, prograss_rate: float, mode="update"):
        url = rest_url_root + Common.REST_URL_DICT.get("infr_progress", "")

        hist_no = job_key.split("_")[-1]

        obj = {
            "infr_hist_no": hist_no,
            "progress_rate": str(prograss_rate),
            "mode": mode
        }

        rst_sttus = RestManager.post(url=url, data=obj, logger=logger)

        return rst_sttus

    @staticmethod
    def set_status(rest_url_root: str, logger: MPLogger.getLogger, job_type, job_key, task_idx, status, message):
        curr_sttus_cd = RestManager.get_status_cd(rest_url_root, logger, job_type, job_key)
        if int(curr_sttus_cd) < int(status):
            RestManager.update_status_cd(rest_url_root, logger, job_type, status, job_key,
                                         task_idx, message)

    @staticmethod
    def set_time(rest_url_root: str, logger: MPLogger.getLogger, job_type, job_key, task_idx, start_or_end):
        if task_idx == "0":
            RestManager.update_time(rest_url_root, logger, job_type, job_key, start_or_end)
