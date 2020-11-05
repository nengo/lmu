"""LMU metapackage (should not be imported directly)."""

import sys

from keras_lmu.layers import LMU, LMUCell, LMUFFT

print(
    "'lmu' is a metapackage that should not be imported directly. You might be "
    "intending to `import keras_lmu` (which used to be generically referred to as "
    "'lmu'). For now this will have the effect of importing 'keras_lmu', but this will "
    "not work in the future so you should update your imports.",
    file=sys.stderr,
)
