from setuptools import setup, find_packages

setup(
    name="ur_material",            # 包的名字
    version="0.1.0",                 # 版本号
    packages=find_packages(where="src"),  # 包的位置
    package_dir={"": "src"},         # 使得源码包在 src 目录下
    install_requires=[               # 外部依赖
        # 例如
        "numpy==1.26.4",
        "augraphy==8.2.6",
        "imgaug==0.4.0",
        "requests>=2.24.0"
    ],
    include_package_data=True,       # 包含其他资源（如静态文件、模板等）
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open('README.md').read(),  # 包含详细描述
    long_description_content_type="text/markdown",  # Markdown 格式
)