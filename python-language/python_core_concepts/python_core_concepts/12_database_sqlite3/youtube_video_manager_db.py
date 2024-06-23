import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()
#  triple quote me jo bhi likho aus ke formatting save rehti ha 
#  jo bhi likho exactly same wahan per  jata ha 

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL 
     )
 ''')
def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 70)
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" * 70)
    print("\n")


def add_video(name ,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()
def update_video(update_id, name ,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name ,time, update_id))
    con.commit()
def del_video(del_id):
    cursor.execute("DELETE FROM videos where id = ?", (del_id,))
    con.commit()

def main():
    while True:
        print("YouTube Manager APP with Sqlite3 as DB")
        print("1. List All Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit Program")

        choice = input("Choose an option from the above given menu: ")

        if choice == '1':
            list_all_videos()
        elif choice =='2':
            name = input("Enter name of youtube video: ")
            time = input("Enter time of youtube video: ")
            add_video(name ,time)
        elif choice =='3':
            update_id = input("Enter id of youtube video that you want to udate: ")
            name = input("Enter name of youtube video: ")
            time = input("Enter time of youtube video: ")
            update_video(update_id, name ,time)
        elif choice =='4':
            del_id = input("Enter id of youtube video that you want to del: ")          
            del_video(del_id)
        elif choice == '5':
            break
        else:
            print("Invalid Input")

    con.close()
        
if __name__ == "__main__":
    main()

