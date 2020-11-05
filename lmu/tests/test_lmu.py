from importlib import reload

import keras_lmu
import lmu


def test_import_fallback(capsys):
    reload(lmu)

    assert (
        "'lmu' is a metapackage that should not be imported" in capsys.readouterr().err
    )

    assert lmu.LMU is keras_lmu.LMU
    assert lmu.LMUCell is keras_lmu.LMUCell
    assert lmu.LMUFFT is keras_lmu.LMUFFT
