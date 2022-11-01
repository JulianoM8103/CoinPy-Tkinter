from cx_Freeze import setup, Executable

base = None    

executables = [Executable("index.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "CoinPy",
    options = options,
    version = "0.0.7",
    description = 'La version Alpha de CoinPy',
    executables = executables
)