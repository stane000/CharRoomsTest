from typing import Optional
import yaml
from dataclasses import dataclass

yml_file = 'params.yml'

@dataclass(frozen=True)
class User:
    email: str
    password: str

@dataclass
class Arguments:

    user: Optional[User]

    
    @classmethod
    def load_users_from_yaml(cls, file_path):

        user = None

        with open(file_path, 'r') as file:
            params_data = yaml.safe_load(file)
        
        for param in params_data:

            if param == "user":
                user =  User(**params_data[param])

        return cls(user)
    

def get_user_tester():
    return Arguments.load_users_from_yaml(yml_file).user

