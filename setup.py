from distutils.core import setup

setup(
    name='BROS',
    version='0.1',
    license="Apache-2.0",
    description='BERT Relying On Spatiality',
    packages_dir=  {
        "bros.train": "train.py",
        "bros.evaluate": "evaluate.py",
        "bros.bros": "bros",
        "bros.lightning_modules": "lightning_modules",
        "bros.model": "model",
        "bros.preprocess": "preprocess",
        "bros.utils": "utils"
    },
    install_requires = [
        "nptyping >= 1.4.2",
        "numpy >= 1.20.3",
        "opencv-python-headless >= 4.5.4.60",
        "pytorch-lightning >= 1.5.6",
        "omegaconf",
        "pillow",
        "six",
        "overrides >= 4.1.2",
        "transformers >= 4.11.3",
        "seqeval >= 0.0.12",
        "imagesize",
        "tensorboard>=2.2.0",
        "torch >= 1.9.1",
        "torchvision >= 0.10.1",    
    ]
)
