import os
import time
from driver import TestDriver
import pytest

def test_login_logout():

    driver = TestDriver()
    driver.login("stankovicigor199737@gmail.com", "E11zje9de")
    assert driver.is_user_logged(), "Failed to login"
    driver.logout()
    assert not driver.is_user_logged(), "Failed to logout"

def test_unsuccessful_login():

    driver = TestDriver()
    driver.login("stankovicigor1997374@gmail.com", "E11zje9de")
    message =  driver.get_messages_info()
    assert message.text == 'user dos not exist\nUser name or password dos not exist', "Error meesage not shown to user after wrong login"

def test_send_meessge():

    driver = TestDriver()
    if not driver.is_user_logged():
        driver.login("stankovicigor199737@gmail.com", "E11zje9de")

    assert driver.is_user_logged(), "User is not logged"

    messages_before = driver.get_all_room_meessges(6)
    driver.send_message(6, "Hey from stane00")
    messages_after  = driver.get_all_room_meessges(6)

    assert len(messages_after)  == len(messages_before) + 1, \
        f"Expected number of messages: {len(messages_before) + 1}, actual: {len(messages_after)}"
    
    assert "Hey from stane00" in messages_after[0].text, f"Hey from stane00 expected to be last message, actual: {messages_after[1].text}"


@pytest.mark.room
@pytest.mark.parametrize("count", [1, 2, 3, 4, 5])
def test_create_room(count):

    driver = TestDriver()
    if not driver.is_user_logged():
        driver.login("stankovicigor199737@gmail.com", "E11zje9de")

    assert driver.is_user_logged(), "User is not logged"
    
    rooms_before = driver.get_number_of_roooms_on_page()

    driver.create_room("New Topic", "Room by selenium", "Ovu sobu je kreirao test")

    rooms_after = driver.get_number_of_roooms_on_page()

    assert rooms_after == rooms_before + 1, f"Wrong number of rooms, expected {rooms_before + 1}, actual {rooms_after}"




if __name__ == "__main__":
    pytest.main(["-v", "-s","-m room", os.path.abspath(__file__)])


