import os
import time
from typing import Any

from progress.bar import ShadyBar

class PackageManager():
    
    def __init__(self) -> None:
        pass
    
    def install(self, name:str) -> None:
        self.create(name=name)
        name = name.lower()
        with ShadyBar('Installing', max=20) as bar:
            for i in range(20):
                time.sleep(0.5)
                bar.next()
                   
        with open(f"packages/{name}/{name}.pkg", "w") as file:
            file.write("package installed")
            
    def uninstall(self, name:str) -> None:
        os.remove(f"packages/{name.lower()}.pkg")
        
    def create(self, name:str) -> None:
        os.makedirs(f"packages/{name}")