# pyinstaller-hooks/hook-caffeine.py
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_dynamic_libs
hiddenimports = collect_submodules('caffeine') 
datas = collect_data_files('caffeine') 
binaries = collect_dynamic_libs('caffeine')