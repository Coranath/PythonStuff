from pythonping import ping
from time import sleep
from os import system

counter = 0
results = [0,0,0,0,0,0,0,0,0,0]
while True:

    result = ping("google.com")
    results[counter] = result
    system("cls")
    print(f"Ping to Google is: Min = {result.rtt_min_ms}ms, Avg = {result.rtt_avg_ms}ms, Max = {result.rtt_max_ms}ms; Packet Loss = {result.packet_loss}")
    avgCount = 0
    avgMin, avgAvg, avgMax, avgPL = [0]*4
    for r in results:
        if r != 0:
            avgCount += 1
            avgMin += r.rtt_min_ms
            avgAvg += r.rtt_avg_ms
            avgMax += r.rtt_max_ms
            avgPL += r.packet_loss
    avgMin = avgMin / avgCount
    avgAvg = avgAvg / avgCount
    avgMax = avgMax / avgCount
    avgPL = avgPL / avgCount
    print(f"Average over the past 10 pings has been: Min = {avgMin:0.2f}ms, Avg = {avgAvg:0.2f}ms, Max = {avgMax:0.2f}ms, Packet Loss = {avgPL:0.1f}")
    sleep(1)
    counter = (counter+1)%10
