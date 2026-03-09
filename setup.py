from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="kta_dogrulama",
    version="1.0.0",
    description="Test ve Form Masası Aparat Doğrulama Kayıt Formu (PTR 07/222-02)",
    author="KTA Endüstri",
    author_email="info@kta.com.tr",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
