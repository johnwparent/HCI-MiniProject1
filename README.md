# HCI-MiniProject1
Clarkson HCI 559 Mini Project 1


## Instructions for data collection:

The only package requirements for this project are Tkinter, Time, random, and the
Python CSV library all of which are Python standard libraries and are packaged
alongside Python distributions as builtins and should require no installation. If for
whatever reason these packages are not present on the system, the user should first
ensure that Python3 version > 3.3 is the Python version executing this code. If that
is the case and there are still issues importing these packages, please reinstall Python on windows and select these packages on installation. On Unix the command `sudo apt-get install python-<pkg_name>` (or substitue apt with a preferred debian package manager) should install whatever packages are needed.

Once dependencies are met, the scripts can be run and data collection can begin.

Two scipts can be found in the scipts directory of this repo. One is named baseline iterface.py and the other test_interface.py.

Each represents an interface to be utilized for data gathering. The baseline_interface.py clearly representing the interface with the provided color palatte and the test_interface providing the interface with an updated palatte. Each script will, once activated, run for exactly three minutes before closing itself. The interfaces can be closed earlier if desired. The scripts will produce one CSV file each, in the directory from which they are executed. These CSV files will contian the data gathered from each run of the script. If multiple runs of the script will be made from the same directory, in order to preserve data from previous runs, it is neccesary to manually rename the data files produced by previous run so they will not be overwritten.

To exectue these files, from a chose directory run ```python3 <name-of-script>``` which will bring up the interface. Further instruction will then be provided by said interface.

#### Collaborators
 - John Parent
 - Owen Talmage
