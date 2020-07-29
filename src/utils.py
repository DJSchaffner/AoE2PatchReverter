# Utils
import sys
import pathlib
import shutil
import locale
import re
from datetime import datetime

def extract_date(date_string):
  """Extract a date in the format of 'd(d) Monthname yyyy'.

  Returns a datetime object
  """

  date_stripped = re.search(r"\d+ \w* \d+", date_string).group(0)
  
  locale.setlocale(locale.LC_TIME, "en_US")
  date = datetime.strptime(date_stripped, "%d %B %Y") 
  locale.setlocale(locale.LC_TIME, "de_DE")

  return date

def check_dotnet():
  """Checks if dotnet is available."""

  return not (shutil.which("dotnet") == None)

def base_path():
  """Construct the base path to the exe / project."""

  # Get absolute path to resource, works for dev and for PyInstaller
  if getattr(sys, 'frozen', False):
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    return pathlib.Path(pathlib.sys.executable).parent
  else:
    return pathlib.Path()

def resource_path(relative_path):
  """Construct the resource patch for a resource."""

  # Get absolute path to resource, works for dev and for PyInstaller
  if getattr(sys, 'frozen', False):
    # PyInstaller creates a temp folder and stores path in _MEIPASS
    base_path = pathlib.Path(pathlib.sys._MEIPASS)
  else:
    base_path = pathlib.Path()

  return base_path / "res" / relative_path

def clear():   
  """Clear the screen of the console."""
  
  _ = os.system('cls')