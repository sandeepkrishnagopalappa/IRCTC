
class Generic_method:

    def click(self,driver,locator):
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).click()

    def send_keys(self,driver,locator,*,values):
        locator_type,locator_value=locator
        driver.find_element(locator_type,locator_value).send_keys(str(values))




