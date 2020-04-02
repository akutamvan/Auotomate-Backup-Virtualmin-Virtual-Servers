from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
print('\n')
print('Welcome to IT Dudes Web Center')
driver.get('https://your_virtualmin_ip:port/')
print('Launching App in Browser')

# Handling Certificate Error
body = driver.find_element_by_xpath('//*[@id="body"]')
print('Handling Certificate Error')
body.send_keys('thisisunsafe')
# comment these 3 lines if you're not getting ssl certificate
# error when you're opening virtualmin in Google Chrome

print('Done')

username = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[1]/input')))
password = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[2]/input')))
signIn = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div[4]/button')))

ActionChains(driver).click(username).send_keys('root').perform()
print('Username Set')
ActionChains(driver).click(password).send_keys('your_root_password').perform()
print('Password Set')
ActionChains(driver).click(signIn).perform()
print('Sign In Clicked')

# Click Backup and Restore
print('Sign In Success')
backupAndRestore = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mCSB_4_container"]/ul[1]/li[33]/a/span')))
driver.execute_script("arguments[0].scrollIntoView();", backupAndRestore)
ActionChains(driver).move_to_element(backupAndRestore).click(backupAndRestore).perform()
print('Clicking Backup and Restore Menu')

# Click Backup Virtual Server
backupVirtualServer = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="global_backup"]/li[3]/a/span')))
driver.execute_script("arguments[0].scrollIntoView();", backupVirtualServer)
ActionChains(driver).move_to_element(backupVirtualServer).click(backupVirtualServer).perform()
print('Clicking Backup Virtual Server')

# Click Featured and Settings
featuredAndSettings = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/form/table[2]/tbody/tr[1]/td/a[2]')))
driver.execute_script("arguments[0].scrollIntoView();", featuredAndSettings)
ActionChains(driver).move_to_element(featuredAndSettings).click(featuredAndSettings).perform()
print('Clicking Featured and Settings')

# Click Select All Virtualmin Features to Backup
selectAllFeaturesToBackup = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hiddendiv_features"]/table/tbody/tr[1]/td[2]/div/a[1]')))
driver.execute_script("arguments[0].scrollIntoView();", selectAllFeaturesToBackup)
ActionChains(driver).move_to_element(selectAllFeaturesToBackup).click(selectAllFeaturesToBackup).perform()
print('Clicking Select All Virtualmin Features to Backup')

# Click Select All Virtualmin Settings to Backup
selectAllVirtualminSettings = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hiddendiv_features"]/table/tbody/tr[2]/td[2]/div/a[1]')))
driver.execute_script("arguments[0].scrollIntoView();", selectAllVirtualminSettings)
ActionChains(driver).move_to_element(selectAllVirtualminSettings).click(selectAllVirtualminSettings).perform()
print('Clicking Select All Virtualmin Settings to Backup')

# Click Destination and Format
destinationAndFormat = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div[2]/form/table[3]/tbody/tr[1]/td/a[2]')))
driver.execute_script("arguments[0].scrollIntoView();", destinationAndFormat)
ActionChains(driver).move_to_element(destinationAndFormat).click(destinationAndFormat).perform()
print('Clicking Destination and Format')

# Filling Backup Information
backupDestination = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dest0_file"]')))
driver.execute_script("arguments[0].scrollIntoView();", backupDestination)
fileName = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
ActionChains(driver).click(backupDestination).send_keys('/daily_server_backup/backup_' + fileName + '.tar.gz').perform()
print('Filling Backup Destination Folder')

# Choosing Single Archieve File
singleArchieveFile = driver.find_element_by_xpath('//*[@id="hiddendiv_dest"]/table/tbody/tr[3]/td[2]/span[1]/label')
driver.execute_script("arguments[0].scrollIntoView();", singleArchieveFile)
ActionChains(driver).move_to_element(singleArchieveFile).click(singleArchieveFile).perform()
print('Choosing Single Archieve File')
print('Ready to Backup')

# Proceed Backup
backupButton = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="now"]')))
ActionChains(driver).click(backupButton).perform()
print('Backup Started')
