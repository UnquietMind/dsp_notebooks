import os
import shutil
from distutils.dir_util import copy_tree

from setuptools import find_packages, setup

import warnings

# global variables
repo_notebook_folder = f'notebooks'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
package_name = 'pystrath_dsp'
pip_name = 'pystrath-dsp'
data_files = []

# check whether board is supported
# Get environment variables
def check_env():
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError(
            "Directory {} does not exist.".format(board_notebooks_dir))

    notebooks_dir = None
    if 'PYNQ_JUPYTER_NOTEBOOKS' not in os.environ:
        warnings.warn(
            "Use `export PYNQ_JUPYTER_NOTEBOOKS=<desired-notebook-path>` "
            "to get the notebooks.",
            UserWarning)
    else:
        notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']

    return notebooks_dir

# copy notebooks to jupyter home
def copy_notebooks():
    board_notebooks_dir = check_env()
    src_nb_dir = os.path.join(repo_notebook_folder)
    dst_nb_dir = os.path.join(board_notebooks_dir, 'dsp-notebooks')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)
copy_notebooks()
setup(
    name=package_name,
    version='0.1',
    install_requires=[
    ],
    author="strath-sdr",
    packages=find_packages(),
    package_data={
        '': data_files,
    },
    description="University of Strathclyde Python SDR.")
