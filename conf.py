# Configuration file for the Sphinx documentation builder.
# For a full list of options, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here. Adjust the path as needed.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate UHC Ucard Online'
copyright = '2025, Activate.UHC.com'
author = 'Activate.UHC.com'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# Favicon
html_favicon = 'favicon.ico'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. 
# These extensions are optional but useful for Read the Docs.
extensions = []

# -- Options for HTML output -------------------------------------------------

# Use the Read the Docs theme for better compatibility
html_theme = 'sphinx_rtd_theme'

# Theme options
html_theme_options = {
    'show_powered_by': False,  # Disable "Powered by Sphinx"
    'collapse_navigation': False,
    'navigation_depth': -1  # No sidebar navigation
}

# Hide the "View page source" link
html_show_sourcelink = False  

# Add paths that contain custom static files (such as style sheets)
# These files are copied after the built-in static files.
html_static_path = ['_static']

# -- Optional: Paths to ignore during the build ------------------------------
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
