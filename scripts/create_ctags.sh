#!/bin/sh

# `not include` virtualenv, eg, `Django1.11` and `3rd package`
# Only include your directory
ctags -R --fields=+l --languages=python --python-kinds=-iv -f tags ./

# include virtualenv, eg, `django1.11` and `3rd package`, 
# but not include `your directory`
ctags -R --fields=+l --languages=python --python-kinds=-iv -f ./tags $(python -c "import os, sys; print(' '.join('{}'.format(d) for d in sys.path if os.path.isdir(d)))")

# Both include virtualenv, eg, `django1.11` and `3rd package`, 
# And  include `your directory`
ctags -R --fields=+l --languages=python --python-kinds=-iv -f ./tags ./ $(python -c "import os, sys; print(' '.join('{}'.format(d) for d in sys.path if os.path.isdir(d)))")
