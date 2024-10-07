import time

class Packet:

    def __init__(self, id, size):  
        self.id = id
        self.size = size

    def getSize(self):
        return self.size

    def getId(self):
        return self.id

class LeakyBucket:
    def __init__(self, leakRate, size):  
        self.leakRate = leakRate
        self.bufferSizeLimit = size
        self.buffer = []
        self.currBufferSize = 0

    def addPacket(self, newPacket):
        if self.currBufferSize + newPacket.getSize() > self.bufferSizeLimit:

            print("Bucket is full. Packet rejected.")
            return

        self.buffer.append(newPacket)

        self.currBufferSize += newPacket.getSize()

        print("Packet with id = " + str(newPacket.getId()) +  " added to bucket.")

    def transmit(self):

        if len(self.buffer) == 0:

            print("No packets in the bucket.")
            return False 


        n = self.leakRate
        while len(self.buffer) > 0:
            topPacket = self.buffer[0]
            topPacketSize = topPacket.getSize()

            if topPacketSize > n:
                break

            n = n - topPacketSize

            self.currBufferSize -= topPacketSize

            self.buffer.pop(0)
            print("Packet with id = " + str(topPacket.getId()) + " transmitted.")
        return True  

if __name__ == '__main__':
    bucket = LeakyBucket(1000, 10000)
    bucket.addPacket(Packet(1, 200))
    bucket.addPacket(Packet(2, 500))
    bucket.addPacket(Packet(3, 400))
    bucket.addPacket(Packet(4, 500))
    bucket.addPacket(Packet(5, 200))
    
    while True:
        has_packets = bucket.transmit()
        if not has_packets:
            break  
        print("Waiting for next tick.")
        time.sleep(1)
