# import keyboard
import time
import threading

runningP = -1

# RN arrays of processes
RN = {
    0: [0, 0, 0, 0, 0],
    1: [0, 0, 0, 0, 0],
    2: [0, 0, 0, 0, 0],
    3: [0, 0, 0, 0, 0],
    4: [0, 0, 0, 0, 0]
}

token = {
    "token_owner": 2,
    "Q": [],
    "LN": [0, 0, 0, 0, 0],
    "isRunning": False
}

def dispCurrentRNState():
    print("Current RN Arrays:")
    for key, value in RN.items():
        print(key, ": ", value)

def updateRN(processNo, sequenceNumber):
    for key, value in RN.items():
        value[processNo] = max(value[processNo], sequenceNumber)

# Execute cs and remaining tasks

def executeCS(processForCS):
    global runningP
    print("\n******************************\n")
    print(f"Process {processForCS} executing CS...")
    print('Token owner is: {}'.format(token["token_owner"]))

    time.sleep(10)
    print(f'\nProcess {processForCS} has completed running CS')

    # Process completed CS
    token["isRunning"] = False

    # update LN
    token["LN"][processForCS] = RN[processForCS][processForCS]

    # Check For Outstanding Requests
    # For every site Sj, whose ID is not present in the token queue Q, it appends its ID to Q if RNi[j] = LN[j] + 1 to indicate that site Sj has an outstanding request.
    for index, val in enumerate(RN[token["token_owner"]]):
        # print("Running P: ", runningP)
        if(val == token["LN"][index] + 1 and index != runningP and index not in token["Q"]):
            # outstanding Requests
            print(f'Process {index}\'s request is outstanding, it will be added to Token\'s Queue')
            token["Q"].append(index)
            print(f'Queue: {token["Q"]}')

    # Handing out the token
    if(len(token["Q"]) != 0):
        # pop a process from the queue and give it the token
        poppedPs = token["Q"].pop(0)
        token["token_owner"] = poppedPs
        token["isRunning"] = True
        executeCS(poppedPs)

if __name__ == "__main__":
    # Display Current State of RN Arrays
    dispCurrentRNState()
    print(" ")
    print('Token owner is: {}'.format(token["token_owner"]))

    while True:

        if(token["isRunning"]):

            processes = input("Enter Process Numbers which want to access C.S separated by space (Click E for Exit): ")
            if processes == 'E':
              break

            if(processes != 'N'):
                psList = processes.strip().split(" ")
                print(" ")

                for ps in psList:
                    processForCS = int(ps)
                    print(f"***** Process {processForCS} *****")
                    seqNo = RN[processForCS][processForCS]+1
                    # Broadcasting Request

                    print(f"Process No.: {processForCS}")
                    print(f"Sequence No.: {seqNo}")
                    print(f"Broadcasting Request ({processForCS} , {seqNo}) .......")
                    time.sleep(2)
                    print("Broadcast complete")
                    print(" ")

                    # Updating RN Arrays
                    print("Updating RN Arrays at all process sites")
                    updateRN(processForCS, seqNo)
                    print("Current RN Arrays: ")
                    dispCurrentRNState()
                    print(" ")

        else:

            processForCS = int(input("Enter Process No. which wants to access C.S: "))
            seqNo = RN[processForCS][processForCS]+1
            # Broadcasting Request

            print(f"Process No.: {processForCS}")
            print(f"Sequence No.: {seqNo}")
            print(f"Broadcasting Request ({processForCS} , {seqNo}) .......")
            time.sleep(2)
            print("Broadcast complete")
            print(" ")

            # Updating RN Arrays
            print("Updating RN Arrays at all process sites")
            updateRN(processForCS, seqNo)
            print("Current RN Arrays: ")
            dispCurrentRNState()
            print(" ")

            # Check condition of sending token: RNj[i] = LN[i] + 1
            if(RN[token["token_owner"]][processForCS] == token["LN"][processForCS] + 1):
                # give the token
                print(f"Conditions met, giving token to {processForCS}...")
                token["token_owner"] = processForCS

                # print(f"New Token Owner: {token["token_owner"]}")
                print('Token owner is: {}'.format(token["token_owner"]))

                token["isRunning"] = True
                runningP = processForCS

                thread = threading.Thread(target=executeCS, args=(processForCS, ))
                thread.start()

                print("Main Continuing Running")
