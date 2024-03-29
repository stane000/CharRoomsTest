import os
import random
import string
import time
from chat_rooms_client import ChatRoomsClient
from driver import TestDriver
import pytest
from hypothesis import Phase, example, given, reproduce_failure, settings, HealthCheck
from hypothesis.strategies import composite, lists, sampled_from, booleans, emails, from_regex, text

from my_decorators import end_test
from params_parser import User, get_user_tester

@pytest.fixture(scope="module")
def driver():
    return TestDriver()

@pytest.fixture(scope="module")
def clinet():
    return ChatRoomsClient()
#----------------------------------------------------------------


@pytest.mark.login_logout
@pytest.mark.parametrize("iterator", range(10))
def test_login_logout(driver: TestDriver, iterator):

    user = get_user_tester()

    driver.login(user.email, user.password)
    assert driver.is_user_logged(), "Failed to login"
    driver.logout()
    assert not driver.is_user_logged(), "Failed to logout"
                          
@pytest.mark.hypo
@example("stankovicigor1997374@gmail.com", "E11zje45de")
@settings(deadline=None, max_examples=20, print_blob=True)
@given(email=emails(), password=text(alphabet=string.ascii_letters, min_size=1, max_size=15))
def test_unsuccessful_login(driver: TestDriver, email, password):
      
    print(password)
    driver.login(email, password)
    message =  driver.get_messages_info()
    assert message.text == 'user dos not exist\nUser name or password dos not exist', \
                             "Error meesage not shown to user after wrong login"
    
@composite
def random_room(draw):
    return draw(sampled_from(ChatRoomsClient().get_rooms()))

@pytest.mark.send
@settings(deadline=None, max_examples=20, print_blob=True)
@given(message=text(min_size=1, max_size=50), room=random_room())
def test_send_meessge(driver: TestDriver, message, room):

    user = get_user_tester()

    if not driver.is_user_logged():
        driver.login(user.email, user.password)

    assert driver.is_user_logged(), "User is not logged"

    random_room_id = room["id"]

    messages_before = driver.get_all_room_meessges(random_room_id)
    driver.send_message(random_room_id, message)
    messages_after  = driver.get_all_room_meessges(random_room_id)

    assert len(messages_after)  == len(messages_before) + 1, \
        f"Expected number of messages: {len(messages_before) + 1}, actual: {len(messages_after)}"
    
    assert message in messages_after[0].text, f"Hey from stane00 expected to be last message, actual: {messages_after[1].text}"

@pytest.mark.room
@pytest.mark.parametrize("counter", range(10))
def test_create_room(driver: TestDriver, counter):

    user = get_user_tester()

    if not driver.is_user_logged():
        driver.login(user.email, user.password)

    assert driver.is_user_logged(), "User is not logged"
    
    rooms_before = driver.get_number_of_roooms_on_page()

    driver.create_room("New Topic", "Room by selenium", "Ovu sobu je kreirao test")

    rooms_after = driver.get_number_of_roooms_on_page()

    assert rooms_after == rooms_before + 1, f"Wrong number of rooms, expected {rooms_before + 1}, actual {rooms_after}"




if __name__ == "__main__":
    pytest.main(["-v", "-s","-m room", os.path.abspath(__file__)])


