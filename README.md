```
in ".venv\Lib\site-packages\tensorflow\python\keras\saving\hdf5_format.py"
replace 
    line 625:
        from tensorflow.python.keras import __version__ as keras_version  # pylint: disable=g-import-not-at-top
    with:
        from keras import __version__ as keras_version

in ".venv\Lib\site-packages\tensorflow\python\keras\engine\training.py"
replace 
    line 2360:
        from tensorflow.python.keras import __version__ as keras_version  # pylint: disable=g-import-not-at-top
    with:
        from keras import __version__ as keras_version

in ".venv\Lib\site-packages\tensorflow\python\keras\engine\data_adapter.py"
replace 
    line 1696:
        return isinstance(ds, input_lib.DistributedDatasetInterface)
    with:
        return isinstance(ds, input_lib.DistributedDatasetSpec)
```

This files doesnt have a model.predict() -- No testing yet of dataset 