# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Tinylab'
copyright = '2024, Tinylab'
author = 'Tinylab'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
# Your other extensions here
    'sphinx_rtd_theme',
]

html_theme = "sphinx_rtd_theme"