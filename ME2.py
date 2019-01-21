from operator import itemgetter
import random

n = int(input("number of nodes: "))

#request_quota = int(input("total number of requests for all nodes: "))


clk = None
LockMsgQue = []
lockmsg = 1
WaitingQue = []
wait = True
FailMsgQue = []
INQsent = False
cur_locking_request = None
in_cs = False
ReleSent = False
locked = False

item = None
Req_list = []
curr_cs = []
runtime = 3
req =0

r =random.random()
node_number = random.randint(0, n)  #randomly assign number from list

# A node enters into one of the four states randomly
for x in runtime:
    node_number = random.randint(0, n)

    if r< 0.25:             # A node will request if system if free

        print( node_number, "is requesting.")
        if (cur_locking_request == None):
            # send(Lock(self), pj)
            cur_locking_request = node_number
            locked = True
            Req_list.append(node_number)
            req+= 1
        elif (INQsent == False):
            WaitingQue.append(node_number)  # in order
            sorted(WaitingQue, key=itemgetter(1))
            item = WaitingQue[0]
            INQsent = True

        else:
            break


    elif (r > 0.25) and (r < 0.5):  # A node will enter cs
        ts = logical_clock()
        if node_number not in curr_cs:
            print("in cs.")
            #for item in R:
            #send(Request(ts, self), item)
            in_cs = True
            curr_cs.append(node_number)
            LockMsgQue.append(node_number)
        else:
            break

        # to exit cs

        in_cs = False
        print("Is releasing.")
        #for item in R:
            #send(Release(self), item)

        INQsent = False
        cur_locking_request = None
        ReleSent = False
        Locked = False


    elif (r > 0.5) and (r < 0.75):  # If in cs, node will release resource
        if (len(WaitingQue) > 0):
            (proc, value) = WaitingQue.pop(0)
            Locked = True
            cur_locking_request = (proc, value)
            send(Lock(self), proc)
        else:
            Locked = False
            cur_locking_request = None
    else:

        # for fail node
    if (node_number) not in list1 or (node_number) not in list2:
        if node_number not in curr_cs or Req_list:
            OnFail(node_number)
            print("failed node: ", node_number)
            FailMsgQue.append(node_number)