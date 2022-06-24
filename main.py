import sys
import time

import psutil

import supervision
from datetime import datetime
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "eLG0Cv_MlOKoMxQPoaWBUzZT5I_g8XuwHJX9CYTZxA-amsN-dIx_ec2_T7VdSnYw4aGAWHyILf_TyB1nJtRlog=="
org = "mael.legrand@edu.itescia.fr"
bucket = "test"


def send_logs(api):
    """
    Send logs to InfluxDB
    :param api: write api
    :return: nothing
    """
    for function in supervision.send_all():
        for data in function:
            api.write(bucket, org, data)
            # print("Sent: " + data)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == "--help":
            print('Use: python main.py -i <interval>')
        if sys.argv[1] == "-i":
            try:
                interval = sys.argv[2]
                while True:
                    with InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token,
                                        org=org) as client:
                        write_api = client.write_api(write_options=SYNCHRONOUS)
                        send_logs(write_api)
                        print(' \n Logs sent to database')
                    client.close()
                    time.sleep(int(interval))
            except Exception as e:
                print('Error: ', e)
    else:
        sys.exit(1)

#
#     write_api = client.write_api(write_options=SYNCHRONOUS)
#     data = "testdata,data=cpu number=8"
#     write_api.write(bucket, org, data)
#     query = """from(bucket: "test") |> range(start: -1h)"""
#     tables = client.query_api().query(query, org=org)
#     for table in tables:
#         for record in table.records:
#             print(record)
#     client.close()
