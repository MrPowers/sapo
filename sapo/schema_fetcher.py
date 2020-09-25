import yaml
import pyarrow as pa


def pyarrow_type(string):
    mapping = {'string': pa.string(), 'int64': pa.int64()}
    return mapping[string]


def yaml_to_pyarrow_schema(path):
    arr = []
    with open(path) as file:
        s = yaml.load(file, Loader=yaml.FullLoader)
        for k, v in s['columns'].items():
            arr.append(pa.field(k, pyarrow_type(v['data_type']), v['nullable']))
    return pa.schema(arr)

