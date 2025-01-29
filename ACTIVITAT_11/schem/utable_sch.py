from typing import List, Dict

def utable_schema(data) -> Dict[str, str]:
    return{
        "punts_actuals": data[0],
        "total_partides": data[1],
        "win_partides": data[2],
        "record_time": data[3],
        "record_punts": data[4]
    }

def utables_schema(datas) -> List[Dict[str, str]]:
    return [utable_schema(data) for data in datas]