from dataclasses import dataclass
from typing import Dict, List, Optional
from requests import Session

@dataclass
class GetResponseList:

    response: Optional[List[Dict]]
    
    @classmethod
    def return_respone(cls, response):
        if response.status_code == 200:
            return  cls(response.json()).response
        else: 
            return cls(None)
        
class ChatRoomsClient:

    def __init__(self) -> None:
        self.domain = "https://stane000.pythonanywhere.com/api/"
        self.session = Session()

    def get_rooms(self) -> Dict:
        response = self.session.get(f'{self.domain}/rooms', verify=False)
        return GetResponseList.return_respone(response)
    
if __name__ == '__main__':


    client = ChatRoomsClient()

    rooms = client.get_rooms()

    a = 5