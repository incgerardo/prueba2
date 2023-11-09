from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #para esperar que se cargue la pagina
from selenium.webdriver.support import expected_conditions as EC #buscar info para ver si existe o no el elemento
from selenium.webdriver.common.by import By #se usa para escoger elementos
from bs4 import BeautifulSoup
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")

driver_path = "C:\\Users\\igelectronica01\\Desktop\\Python\\scraping\\chromedriver-win64\\chromedriver.exe"

# Inicializa el controlador del navegador (por ejemplo, Chrome)
driver = webdriver.Chrome(options=opt)
time.sleep(1)

url="https://www.walmart.com/browse/feeding/baby-food/5427_133283_1001448?povid=EDN_EDNCP_x_LHN_CategoriesBaby_BabyFood&affinityOverride=default&page=1"

# Carga una página web
driver.get(url)

link = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.absolute.w-100.h-100.z-1.hide-sibling-opacity")))
time.sleep(30)
link.click()
time.sleep(20)