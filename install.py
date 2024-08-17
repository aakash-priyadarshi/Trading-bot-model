import subprocess

def install_package(package):
    try:
        # Try to install with the specified version
        subprocess.run(f"pip install {package}", check=True, shell=True)
    except subprocess.CalledProcessError:
        # If the installation fails, try installing the package without version constraints
        package_name = package.split('==')[0]
        print(f"Failed to install {package}. Trying to install the latest version of {package_name}...")
        subprocess.run(f"pip install {package_name}", check=True, shell=True)

# Read the requirements.txt file
with open("requirements.txt", "r") as file:
    lines = file.readlines()

# Install each package
for line in lines:
    package = line.strip()
    if package and not package.startswith("#"):
        install_package(package)
