from applium.find_element.capability import driver,check_cancle, check_skip

check_cancle()
check_skip()
driver.find_element_by_class_name('android.widget.EditText').send_keys('自学网2018')
driver.find_element_by_class_name('android.widget.EditText').send_keys('zxw2018')
driver.find_element_by_class_name('android.widget.Button').click()
