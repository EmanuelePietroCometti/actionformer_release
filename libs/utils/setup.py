from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension


setup(
    name='nms_1d_cpu',
    ext_modules=[
        CppExtension(
            name = 'nms_1d_cpu',
            sources = ['./csrc/nms_cpu.cpp'],
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
