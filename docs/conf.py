import os
import sys

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx_rtd_theme',
]
source_suffix = '.rst'
master_doc = 'index'

project = u'Confuse'
copyright = u'2012, Adrian Sampson'

version = '1.3'
release = '1.3.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'Confusedoc'
