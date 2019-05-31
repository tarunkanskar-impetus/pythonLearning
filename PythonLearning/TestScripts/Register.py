from selenium import webdriver
from selenium.webdriver.support.ui import Select


username = "kanskartarun07@gmail.com"



driver = webdriver.Chrome(executable_path='D:/Setups/chromedriver_win32/chromedriver.exe')
driver.get("http://ec2-18-223-116-199.us-east-2.compute.amazonaws.com/")
driver.set_page_load_timeout(10)
driver.maximize_window()
driver.implicitly_wait(30)

#Click register link
driver.find_element_by_link_text('Register here').click()
driver.get_screenshot_as_file('D:/PythonWorkSpace/Registration.png') 


# Fill registration form and submit
driver.find_element_by_id('id_username').send_keys(username)
driver.find_element_by_id('id_first_name').send_keys('First Name')
driver.find_element_by_id('id_last_name').send_keys('last Name')
driver.find_element_by_id('id_email').send_keys('tarun.kanskar2@impetus.co.in')
driver.find_element_by_id('id_password1').send_keys('python@123')
driver.find_element_by_id('id_password2').send_keys('python@123')
driver.find_element_by_id('id_address').send_keys('impetus IT Park')
driver.find_element_by_id('id_phone_number').send_keys('+1-541-754-3010')
driver.find_element_by_id('id_dob').send_keys('07/06/1989')
driver.find_element_by_id('id_profession').send_keys('Sr. Test Engineer')
driver.find_element_by_id('id_region_to').send_keys('India')
driver.find_element_by_name('submit').click()


