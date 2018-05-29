# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os


sys.path.insert(0,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/docs/source/../../src')
sys.path.insert(1,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/docs/source/../')
sys.path.insert(2,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/docs/source/../../')
sys.path.insert(3,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/docs/source/../../../')
sys.path.insert(4,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/docs/source/../../../../')
sys.path.insert(5,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts')
# this one is good
sys.path.insert(6,'/home/docs/checkouts/readthedocs.org/user_builds/')
sys.path.insert(7,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/src')

sys.path.insert(8,'/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/src')
sys.path.insert(9,'/../../')

sys.path.insert(10,'/home/docs/checkouts/readthedocs.org/user_builds/')


print("trying to import mpathic in conf.py")
import mpathic
#print(dir(mpathic))


'''
print("print cwd path: ", os.getcwd())
print("printing cwd path contents: ",os.listdir(os.getcwd()))

print("print path 1: /home/docs/checkouts/readthedocs.org/user_builds/ " )
print("printing path 1 contents: ",os.listdir('/home/docs/checkouts/readthedocs.org/user_builds/'))

print("print path 2: /home/docs/checkouts/readthedocs.org/user_builds/mpathic/ " )
print("printing path 2 contents: ",os.listdir('/home/docs/checkouts/readthedocs.org/user_builds/mpathic/'))

print("print path 3: /home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/ " )
print("printing path 3 contents: ",os.listdir('/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/'))

print("print path 4: /home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/ " )
print("printing path 4 contents: ",os.listdir('/home/docs/checkouts/readthedocs.org/user_builds/mpathic/checkouts/latest/'))
'''

#autodoc_mock_imports = ['Bio']
#autodoc_mock_imports = ['qc']
#autodoc_mock_imports = ['mpmath']
#autodoc_mock_imports = ['cStringIO']

# -- Project information -----------------------------------------------------

project = 'mpathic'
copyright = '2018, Ammar Tareen, William Ireland, Justin Kinney'
author = 'Ammar Tareen, William Ireland, Justin Kinney'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# to hide methods/ remove warnings
numpydoc_show_class_members = False

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'numpydoc'
 ]

autodoc_mock_imports = ['cStringIO',
                        'cvxopt',
                        'Bio',
                        'qc',
                        'pymc',
                        'fast'
                        ]

'''
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]
'''

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'bizstyle'
html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'mpathicdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'mpathic.tex', 'mpathic Documentation',
     'Ammar Tareen, William Ireland, Justin Kinney', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mpathic', 'mpathic Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'mpathic', 'mpathic Documentation',
     author, 'mpathic', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True