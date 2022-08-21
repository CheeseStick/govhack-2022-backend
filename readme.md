# PipeWatch API Service (GovHack 2022)

PipeWatch is a holistic platform that provides the stormwater network using machine learning to allow users to check the water performance with early warning systems and helps to make informed decisions that can provide reactive approaches to mitigate flood events.

## Installation

1. Clone the project to local
```bash
git clone https://github.com/CheeseStick/govhack-2022-backend
```

2. Create virtual environment
```bash
virtualenv -p python3.9 venv
```

3. Activate virtual environment
```bash
source venv/bin/activate
```

4. Install dependent packages
```bash
pip install -r requirements.txt
```

5. Download required dataset from [here](https://catalogue.data.govt.nz/dataset/canterbury-stormwater-pipelines1) and save under `Fixture Helper/stormwater` with a name `data.geojson`
```bash
curl https://opendata.canterburymaps.govt.nz/datasets/ecan::canterbury-stormwater-pipelines.geojson --output "Fixture Helper/stormwater/data.geojson"
```

7. Generate fixture from dataset
```bash
python Fixture Helper/stormwater/generate_fixture.py
```

7. Move generated fixture to `PipeNetwork/fixtures/three_water_data.json`
```bash
mv fixtures.json ../../PipeNetwork/fixtures/three_water_data.json
```

8. Migrate DB
```bash
python manage.py migrate
```

9. Start Server
```bash
python manage.py runserver
```

## Contributors
[Jun Jung](https://github.com/CheeseStick)

[Lite Kim](https://github.com/94lite)

[SeongRok Shin](https://github.com/Seongrok-Shin)


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Disclaimer

Data sets used in this project may have different license. Please check before using them.
