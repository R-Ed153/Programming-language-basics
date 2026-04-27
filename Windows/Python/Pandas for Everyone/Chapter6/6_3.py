from pathlib import Path

billboard_data_files = (Path(".").glob("data/billboard-by_week/billboard-*.csv"))
billboard_data_files = sorted(list(billboard_data_files))

print(billboard_data_files)