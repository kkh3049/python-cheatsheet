def get_directory_from_filepath(filepath: str):
  """ Path/to/file.txt => Path/to/ """
  import os
  return os.path.dirname(filepath)

def get_filename_from_filepath(filepath: str):
  """ Path/to/file.txt => file """
  """ Path/to/file.tar.gz => file.tar """
  from pathlib import Path
  return Path(filepath).setm
