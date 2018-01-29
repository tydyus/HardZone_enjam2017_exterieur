
from cx_Freeze import setup, Executable


# On appelle la fonction setup

setup(

    name = "HardZone",

    version = "0.2.1",

    description = "Enjam2017",

    executables = [Executable("main.py")])

