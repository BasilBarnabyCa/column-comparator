# Creating Environments with Python
python -m venv env
source env/bin/activate

# or

python3 -m venv env
source env/bin/activate

# Creating Environments with Conda
conda create -n langchain-env python=3.8
conda activate langchain-env

# Installing requirements
pip install -r requirements.txt