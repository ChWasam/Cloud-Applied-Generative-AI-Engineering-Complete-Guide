import requests
import json

def load_user_data():
    try:
        with open("User_data.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def enter_user_data_to_file(users):
    with open("User_data.txt",'w') as file:
        json.dump(users,file)

def list_of_users(users):
    print('\n')
    print('*' * 70)
    for user in users:
        # print(user)
        print(f"User Name: {user['User Name']} \n User Age: {user['User Age']} \n")
    print('\n')
    print('*' * 70)

def get_data_from_url():
    url ='https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = requests.get(url)
    data =  response.json()

    if data["success"] and 'data' in  data:
        user_data = data["data"]
        user_name = user_data["login"]['username']
        user_age = user_data['dob']['age']
        return user_name ,user_age
    else:
        raise Exception('Failed to fetch user data ')
    

def main():
    users = load_user_data()
    try:
        list_of_users(users)
        user_name , user_age = get_data_from_url()
        print('\n')
        print('Current Users')
        print(f"Username : {user_name} \n" )
        print(f"UserAge : {user_age}" )
        users.append({'User Name' :user_name, 'User Age' : user_age })
        enter_user_data_to_file(users)


    except Exception as e:
        print(str(e))

    

if __name__ == "__main__":
    main()





