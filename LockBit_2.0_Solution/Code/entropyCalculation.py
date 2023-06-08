import os
from dotenv import load_dotenv
import math
import shutil

load_dotenv()

files_dir = os.getenv("FILES")
success_dir = os.getenv("SUCCESS") 

def H(data):
  if not data:
    return 0
  entropy = 0
  for x in range(256):
    p_x = float(data.count(bytes([x])))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
  return entropy

maxent, minent = 0.0, 8.0
maxfile, minfile = None, None

for curdir, dirs, files in os.walk(files_dir):   
    for filename in files:
        curfile = os.path.join(curdir, filename)
        print(curfile)
        try:
            with open(curfile, "rb") as contents:
                entropy = H(contents.read())
                print(entropy)
                if entropy>5:
                    shutil.move(files_dir, success_dir)
                    print("moved")
        except (FileNotFoundError, PermissionError, OSError) as exc:
            print(f"{curfile}: skipped: {exc}")

print(f"max entropy {maxent} ({maxfile})")
print(f"min entroy {minent} ({minfile})")
