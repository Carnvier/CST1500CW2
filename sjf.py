#Shortest Job First

def sjf(process_list):
    t = 0
    gantt = []
    completed = {}

    while process_list != []
        available = []
        for p in process_list:
            if p[1] <= t:
                available.append(p)
        #no processes available
        if available == []
            t += 1
            gantt.append("idle")
            continue
        else:
            available.sort()
            process = available[0]
            #service the process
            burst_time = process[0]
            pid = process[2]
            arrival_time = process[1]
            t += burst_time
            gant..append(pid)
            ct = t
            tt = ct - arrival_time
            wt = tt - burst_time
            process_list.remove(process)
            completed[pid] = [ct,tt,wt]
    print(gantt)
    print(completed)

if __name__ == "__main__":
    process_list =[[6,2,"p1"],[2,5,"p2"],[8,1,"p3"],[3,0,"p4"],[4,0,"p5"]]