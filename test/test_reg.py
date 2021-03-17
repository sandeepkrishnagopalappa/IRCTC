import pytest
import time
from pom.register import Register
from Library.basefixture import Driver_init


class Test_demo(Driver_init):

    def test_object(self):

        obj = Register(self.driver)
        obj.alert_ok()
        obj.click_on_flight()
        obj.window_switch()
        obj.round_trip()
        obj.station_from_sending_keys()
        obj.station_from_click()
        obj.station_to_sending_keys()
        obj.station_to_click()
        obj.start_date_select()
        obj.return_date_click()
        obj.apirl_month_select()
        obj.return_date_select()
        obj.search()
        obj.book_button_check()
        obj.book()
        #obj.normal_fair()
        obj.gst_pop_up_check()
        obj.gst_pop_up()
