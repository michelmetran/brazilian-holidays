"""
Pastas
jun.23
"""


from pathlib import Path

project_path = Path(__file__).parents[2].resolve()

# Data
data_path = project_path / 'data'
data_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
