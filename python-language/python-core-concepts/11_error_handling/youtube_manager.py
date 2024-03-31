import json  
def load_file():
    try:
        with open("youtube.txt","r") as file:
            content_in_load_file = json.load(file)
            # print(content_in_load_file)
            return content_in_load_file

    except FileNotFoundError:
        return []
    
def file_update_helper(videos):
    with open("youtube.txt","w") as file:
        return json.dump(videos, file)
def list_of_videos(videos):
    print("\n")
    print("*" * 70)

    for index,video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    print("\n")
    print("*" * 70)
    print("\n")
    print("\n")

def add_video(videos):
    name = input("Enter name of video")
    time = input("Enter total time of video")
    videos.append({"name":f"{name}","time":f"{time}"})
    file_update_helper(videos)

def update_video(videos):
    list_of_videos(videos)
    seleced_option = int(input("Choose an option from above menu which you want to update"))
    
    if 1<= seleced_option<=len(videos):
        updated_name = input("Enter updated_name of video")
        updated_time = input("Enter total updated_time of video")
        videos[seleced_option - 1] = {"name":f"{updated_name}","time":f"{updated_time}"}
        file_update_helper(videos)
    else:
        print("Invalid Input-choose from the above given menu")

def delete_video(videos):
    list_of_videos(videos)
    seleced_option = int(input("Choose an option from above menu which you want to delete"))
    if 1<= seleced_option<=len(videos):
        del videos[seleced_option - 1]
        file_update_helper(videos)
    else:
        print("Invalid Input-choose from the above given menu")

def main(): 
    while True:
        videos = load_file()
        print("Youtube Video Manager App - Choose an option")
        print("1. Here is the list of available videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit a program")

        choice = input("Enter an option from the above given menu")

        match choice:
            case '1':
                list_of_videos(videos)
                # print(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Input")
    
if __name__ == "__main__":
    main()

        