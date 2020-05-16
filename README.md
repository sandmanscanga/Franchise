# Franchise
Automatic Fantasy Football Stat Tracking Application

## Setup / Install

```bash
git clone https://github.com/sandmanscanga/Franchise.git
cd Franchise
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd franchise
cd core
python3 loader.py --wipe
python3 loader.py --build
python3 loader.py --reload
python3 loader.py --get-logos
python3 loader.py --get-headshots  # <- this takes a few minutes to complete
python3 ../manage.py runserver
## Open browser and visit http://localhost:8000
```

![Worflow Screenshot](docs/images/workflow.png)

![Front-End Example Screenshot](docs/images/front-end-example.png)
