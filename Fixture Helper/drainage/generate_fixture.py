import json

from dataclasses import dataclass
from lib2to3.pgen2.parse import ParseError

from typing import List, Union, Dict
from typing import OrderedDict as OrderedDictType
from collections import OrderedDict


###
# Django Fixture Helper
###
class ModelFixture:
    def get_model(self) -> str:
        raise NotImplementedError("Model is not implemented!")

    def get_fixture(self) -> dict:
        raise NotImplementedError("Get fixture is not implemented")


@dataclass
class DrainageModel(ModelFixture):
    id: int
    name: str

    start_latitude: float
    start_longitude: float

    end_latitude: float
    end_longitude: float

    width: float

    above_high_tide: int
    below_high_tide: int

    def get_model(self) -> str:
        return "DrainageLitter.Drainage"

    def get_fixture(self) -> dict:
        return {
            "model": self.get_model(),
            "pk": self.id,
            "fields": {
                "name": self.name,
                "start_latitude": self.start_latitude,
                "start_longitude": self.start_longitude,
                "end_latitude": self.end_latitude if self.end_latitude != 0 else self.start_latitude,
                "end_longitude": self.end_longitude if self.end_longitude != 0 else self.start_longitude,
                "width": self.width,
                "above_high_tide": self.above_high_tide,
                "below_high_tide": self.below_high_tide
            }
        }

###
# Dictionary Helper
###
def get_str_from_dict(d: dict, k: str, default: str = "Unknown") -> str:
    if k in d and d[k] is not None:
        v = str(d[k])

        if 0 < len(v) and not v.isspace():
            return v
    
    return default

def get_int_from_dict(d: dict, k: str, default: int = 0) -> int:
    if k in d and d[k] is not None:
        try:
            v = int(d[k])
            return v
        
        except ValueError:
            return default

    return default

def get_float_from_dict(d: dict, k: str, default: float = 0.0) -> float:
    if k in d and d[k] is not None:
        try:
            v = float(d[k])
            return v
        
        except ValueError:
            return default

    return default

###
# Main codes
###
fixtures = list()

with open("./GetSurveyAreas.json", "rt") as src_file:
    src_data = json.loads(src_file.read())

    print(f"Data loaded. Total: {len(src_data)}")

    src_file.close()

    for tmp_data in src_data:
        drainage = DrainageModel(
            id=int(tmp_data["id"]),
            name=get_str_from_dict(tmp_data, "name"),
            start_latitude=get_float_from_dict(tmp_data, "latitudeStart"),
            start_longitude=get_float_from_dict(tmp_data, "longitudeStart"),
            end_latitude=get_float_from_dict(tmp_data, "latitudeEnd"),
            end_longitude=get_float_from_dict(tmp_data, "longitudeEnd"),
            width=get_float_from_dict(tmp_data, "widthMeters"),
            above_high_tide=get_int_from_dict(tmp_data, "aboveHighTideMeters"),
            below_high_tide=get_int_from_dict(tmp_data, "belowHighTideMeters")
        )

        fixtures.append(drainage.get_fixture())
    
    with open("./fixture.json", "w") as dest:
        dest.write(json.dumps(fixtures, indent=4))
        dest.close()
