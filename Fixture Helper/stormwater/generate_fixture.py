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
class PipeModel(ModelFixture):
    id: int
    asset_id: str

    pipe_type: str
    length: float
    shape_length: float
    district: str

    diameter: int
    material: str
    depth: float

    def get_model(self) -> str:
        return "PipeNetwork.Pipe"

    def get_fixture(self) -> dict:
        return {
            "model": self.get_model(),
            "pk": self.id,
            "fields": {
                "asset_id": self.asset_id,
                "pipe_type": self.pipe_type,
                "length": self.length,
                "shape_length": self.shape_length,
                "district": self.district,
                "diameter": self.diameter,
                "material": self.material,
                "depth": self.depth
            }
        }

@dataclass
class PipeGeometryModel(ModelFixture):
    pipe: PipeModel
    latitude: float
    longitude: float
    level: float

    def get_model(self) -> str:
        return "PipeNetwork.PipeGeometry"

    def get_fixture(self) -> dict:
        return {
            "model": self.get_model(),
            "fields": {
                "pipe": self.pipe.id,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "level": self.level
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

with open("./data.geojson", "rt") as src_file:
    src_data = json.loads(src_file.read())
    src_data = src_data["features"]

    print(f"Data loaded. Total: {len(src_data)}")

    src_file.close()

    for tmp_data in src_data:
        prop = tmp_data["properties"]
        geometry = tmp_data["geometry"]

        pipe = PipeModel(
            id=int(prop["OBJECTID"]),
            asset_id=get_str_from_dict(prop, "AssetID"),
            pipe_type=get_str_from_dict(prop, "Type"),
            diameter=get_int_from_dict(prop, "Diameter"),
            material=get_str_from_dict(prop, "Material"),
            length=get_float_from_dict(prop, "Length"),
            district=get_str_from_dict(prop, "District"),
            depth=get_float_from_dict(prop, "Depth"),
            shape_length=get_float_from_dict(prop, "Shape__Length")
        )

        if geometry is not None and "coordinates" in geometry:
            try:
                geometries = [PipeGeometryModel(
                    pipe=pipe,
                    longitude=float(geometry[0]),
                    latitude=float(geometry[1]),
                    level=float(geometry[2]),
                    )
                    for geometry in geometry["coordinates"]]

            except Exception as e:
                print(f"Found unexpected value while parsing: {pipe.id}")
                print(geometry)
            
            else:
                fixtures.append(pipe.get_fixture())
                fixtures.extend([g.get_fixture() for g in geometries])
        
        else:
            print(f"Found nil from pipe: {pipe.id}")
    
    with open("./fixture.json", "w") as dest:
        dest.write(json.dumps(fixtures, indent=4))
        dest.close()
