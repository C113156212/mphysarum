from selenium import webdriver
from core.base import ActionComposite
from core.factory import ActionFactory
from core.physarum import Physarum

jsonPath1 = r"yourAddr\config\elearning.json"
jsonPath2 = r"yourAddr\config\zuvio.json"

physarum = Physarum()
physarum.load_json(jsonPath1)
physarum.run()

physarum.load_json(jsonPath2)
physarum.run()

print('done')