# H4J2TbITmyCs_1zWKe9aikteIr2jH6VtyRxrglLmqiIc2cKyj1gG3VQ5HsSRXDz_edUiYRd_oS6carLPvDGeSA==

from datetime import datetime
import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "eLG0Cv_MlOKoMxQPoaWBUzZT5I_g8XuwHJX9CYTZxA-amsN-dIx_ec2_T7VdSnYw4aGAWHyILf_TyB1nJtRlog=="
org = "mael.legrand@edu.itescia.fr"
bucket = "test"

with InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    data = "testdata,data=cpu number=8"
    write_api.write(bucket, org, data)
    query = """from(bucket: "test") |> range(start: -1h)"""
    tables = client.query_api().query(query, org=org)
    for table in tables:
        for record in table.records:
            print(record)
    client.close()



