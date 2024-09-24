import threading
import time
def update_db():
    print("Updating db..")
    time.sleep(3)
    print("Updated DB")
def test(num):
    for i in range(1,num+1):
        print(i,end=" ")
# update_db()
thread_db = threading.Thread(target=update_db)
thread_db.start()
td_n = threading.Thread(target=test,args=(5,))
td_n.start()
#test(5)

print("\n",threading.active_count())
print(threading.enumerate())  #
thread_db.join()
print("bye")