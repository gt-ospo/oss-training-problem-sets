# Note to students:
# DO NOT remove this file, or else nbgrader test cases will automatically fail
# Not all nbgrader tests utilize these functions

import subprocess
import os

# Any bash error (CalledProcessError) will propogate upwards
# Note: expectedOutput accepts strings and lists of strings
def compareOutToString(userCmd, errorMsg, expectedOutput, checkExist = True):
    subprocess.run(["rm", "-rf", ".ipynb_checkpoints"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # remove .ipynb_checkpoints folder to prevent disruptions to staging
    shellOutput = subprocess.check_output(userCmd, shell = True, text = True)
    outFormat = expectedOutput
    if isinstance(expectedOutput, str): # enforce list
        outFormat = [expectedOutput]
    for cStr in outFormat:
        if ((cStr not in shellOutput and checkExist) or (cStr in shellOutput and not checkExist) or "fatal" in shellOutput):
            raise AssertionError(f"Your Output: {shellOutput}\nExpected Output: ...{expectedOutput}...\nError: {errorMsg}")
    print("Success!")

# Compare the hashes of two different endpoints, throws error if not equal: e.g. origin/main
def gitHashCompare(cp1, cp2, errorMsg):
    sOut1 = subprocess.check_output(f"git rev-parse {cp1}", shell = True, text = True)
    sOut2 = subprocess.check_output(f"git rev-parse {cp2}", shell = True, text = True)
    if (sOut1 != sOut2):
        raise AssertionError(f"errorMsg")
    print("Success: Hash Equality")

def changeDirectory(relPath):
    try:
        os.chdir(relPath)
    except FileNotFoundError:
        print("chdir Error: currently in directory: " + str(relPath.cwd()))
    else:
        print("Currently in: " + str(relPath.cwd()))

