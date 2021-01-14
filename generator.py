import pandas as pd
import uuid

est_running_time_in_years = 0.5
number_of_objects = int(est_running_time_in_years * 365 * 24 * 3600 * 100)

number_of_different_paths = 10 ** 4
output_file_ccdb_paths_name = "ccdb_paths.csv"

with open(output_file_ccdb_paths_name, "w+") as output_fh:
    for i in range(number_of_different_paths):
        output_fh.write(f"{i};{str(uuid.uuid1(clock_seq=i))}\n")

output_file_ccdb_name = "ccdb.csv"

with open(output_file_ccdb_name, "w+") as output_fh:
    for i in range(number_of_objects):
        if i % 100000 == 0:
            print(i * 1.0 / number_of_objects * 100, "%", i, "/", number_of_objects)
        # id: uuid, pathid: int, validity: tsrange, create time: bigint, replicas: int[], size: bigint, md5: uuid, contenttype: int, uploadedfrom: inet, initial validity: bigint, metadata: hstore, lastmodified: bigint
        output_fh.write(f"{str(uuid.uuid1(clock_seq=i))};{i % number_of_different_paths};[2010-01-01 14:45, 2010-01-01 15:45);0;[0];0;null;0;null;0;null;0\n")