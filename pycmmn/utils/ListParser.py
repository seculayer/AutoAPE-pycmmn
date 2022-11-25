# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2022 AI Service Model Team, R&D Center.
from typing import List
from pycmmn.utils.JSONUtils import JSONUtils


class ListParser(object):
    @classmethod
    def parse(cls, data: str) -> List:
        try:
            if isinstance(data, list):
                return data
            return JSONUtils.ujson_load(data)
        except Exception as e:
            return data.split(",")

    @staticmethod
    def _str_json(data: str) -> List:
        result = list()
        is_start = False
        is_json = False
        value_str = ""
        for idx, s in enumerate(data[1:-1]):
            if s == "\"":
                if value_str == "":
                    is_start = True
                elif not is_json:
                    result.append(value_str + "\"")
                    value_str = ""
                    is_start = False
            elif s == "{":
                is_json = True
            elif s == "}":
                is_json = False
            if is_json or (is_start and s != ","):
                value_str += s
        return result


if __name__ == '__main__':
    _data = {"vtdpopularity": "[\"{}\"]", "qclass_name": "C_INTERNET", "dns_type": "query",
            "src_hash": "vhFPOSw+qKPYuJ4KufhllA\u003d\u003d", "vtdsubdomains_count": "[\"1\"]",
            "tag_similr_val": "coupang.com", "domain_country_code": "US", "query_ip": "50.118.210.105",
            "vtdsubdomains_certificate_not_before": "[\"2019-09-16 12:28:52\"]", "simhash_score": "36",
            "vtdlast_dns_records_type": "[\"NS\",\"NS\",\"A\",\"SOA\"]", "src_country_code": "SK", "tag_ctas": "N",
            "network_type_cd": "3",
            "vtdlast_dns_records_value": "[\"ns55.domaincontrol.com\",\"ns56.domaincontrol.com\",\"50.118.210.105\",\"ns55.domaincontrol.com\"]",
            "dstn_ip": "164.124.101.2", "AA": "false", "mal_similr_val": "inamban.com",
            "original_log": "{\"ts\":1669081997.44809,\"uid\":\"CckZqA1amcWdKcMo4c\",\"id.orig_h\":\"212.5.212.82\",\"id.orig_p\":33733,\"id.resp_h\":\"164.124.101.2\",\"id.resp_p\":53,\"proto\":\"udp\",\"trans_id\":23466,\"query\":\"byepang.com\",\"qclass\":1,\"qclass_name\":\"C_INTERNET\",\"qtype\":1,\"qtype_name\":\"A\",\"AA\":false,\"TC\":false,\"RD\":true,\"RA\":false,\"Z\":0,\"rejected\":false}",
            "vtdsubdomains_certificate_not_after": "[\"2019-12-15 12:28:52\"]", "recv_time": "20221122105330",
            "detect_hist_no": "1", "query": "byepang.com", "duplicate": "N", "dstn_country_code": "KR",
            "eqp_dt": "20221122110228", "vtdwhois_registrar": "GoDaddy.com, LLC", "alive_status": "Y",
            "vtdsubdomains_last_analysis_stats": "[\"{\\\"malicious\\\":0,\\\"undetected\\\":0,\\\"suspicious\\\":0,\\\"harmless\\\":95,\\\"timeout\\\":0}\"]",
            "RA": "false", "agent_ip": "192.168.60.5", "tag_ai_domain_score": "0.5224",
            "domain_country_name": "United States", "RD": "true", "mal_simhash_score": "22.0",
            "vtdlast_https_certificate_not_after": "[\"2019-12-15 12:34:04\"]",
            "vtdlast_analysis_stats": "[\"{\\\"malicious\\\":0,\\\"undetected\\\":13,\\\"suspicious\\\":0,\\\"harmless\\\":83,\\\"timeout\\\":0}\",\"{\\\"malicious\\\":0,\\\"undetected\\\":13,\\\"suspicious\\\":0,\\\"harmless\\\":83,\\\"timeout\\\":0}\"]",
            "vtdsubdomains_list": "[\"www.byepang.com\"]",
            "vtdlast_https_certificate_not_before": "[\"2019-09-16 12:34:04\"]", "mal_leven_score": "6.0",
            "qtype_name": "A", "tag_manual": "N", "tag_ti": "N", "eqp_ip": "192.168.60.5", "qtype": "1",
            "rejected": "false", "prtc": "udp", "vtdwhois_update_date": "2022-10-19T09:04:59Z", "trans_id": "23466",
            "tag_similr": "Y", "dstn_country_name": "South Korea", "src_ip": "212.0.0.0",
            "vt_whois": "{\"Registrar Abuse Contact Email\":\"abuse@godaddy.com\",\"Registrar URL\":\"http:\\/\\/www.godaddy.com\",\"Registrar Abuse Contact Phone\":\"480-624-2505\",\"Registrar IANA ID\":\"146\",\"Creation Date\":\"2021-04-09T19:15:50Z\",\"Name Server\":\"NS55.DOMAINCONTROL.COM | NS56.DOMAINCONTROL.COM\",\"DNSSEC\":\"unsigned\",\"Registrar WHOIS Server\":\"whois.godaddy.com\",\"Registrar\":\"GoDaddy.com, LLC\",\"Domain Status\":\"clientDeleteProhibited https:\\/\\/icann.org\\/epp#clientDeleteProhibited | clientRenewProhibited https:\\/\\/icann.org\\/epp#clientRenewProhibited | clientTransferProhibited https:\\/\\/icann.org\\/epp#clientTransferProhibited | clientUpdateProhibited https:\\/\\/icann.org\\/epp#clientUpdateProhibited\",\"Registry Domain ID\":\"2604083690_DOMAIN_COM-VRSN\",\"Updated Date\":\"2022-10-19T09:04:59Z\",\"Domain Name\":\"BYEPANG.COM\",\"Registry Expiry Date\":\"2023-04-09T19:15:50Z\"}",
            "uid": "CckZqA1amcWdKcMo4c", "log_type": "20", "in_out": "out",
            "vtdtotal_votes": "[\"{\\\"malicious\\\":0,\\\"harmless\\\":0}\"]", "jaro_score": "0.82",
            "connect_ip": "192.168.60.5", "Z": "0", "qclass": "1", "key": "LG-Col2_2022112210533016266",
            "src_country_name": "Slovakia", "eqp_asset_group_cd": "1", "mal_similr": "Y",
            "tag_ai_trfic_score": "0.5224", "vtdwhois_create_date": "2021-04-09T19:15:50Z", "dstn_port": "53",
            "TC": "false", "src_port": "33733", "learn_hist_no": "99713610732800345", "normalize_result": "000",
            "tag_ai_domain": "N", "data_type": "SECURITY_LOG",
            "vtdlast_dns_records_TTL": "[\"3600\",\"3600\",\"600\",\"3600\"]", "mal_jaro_score": "0.71",
            "log_dt": "20221122105317", "mal_dga": "N", "leven_score": "0.73", "tag_ai_trfic": "N",
            "vtdwhois_expiry_date": "2023-04-09T19:15:50Z"}

    for _ in ListParser.parse(_data.get("vtdlast_analysis_stats")):
        print(_, json.loads(_))
    print(ListParser.parse(_data.get("vtdlast_dns_records_TTL")))

