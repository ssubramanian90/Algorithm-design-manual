'''We have 1,000 data items to store on 1,000 nodes. Each node can store
copies of exactly three different items. Propose a replication scheme to
minimize data loss as nodes fail. What is
the expected number of data entries that get lost when three random nodes fail?
Ans3:
USe RAID
striping and dedicates one drive to storing parity information.
 Data recovery is accomplished by calculating the exclusive OR (XOR) of the
 information recorded on the other drives.
'''
