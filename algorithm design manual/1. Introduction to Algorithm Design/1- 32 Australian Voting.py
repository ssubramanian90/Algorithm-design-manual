#Australian ballots require that voters rank all the candidates in order of
#choice. Initially only the first choices are counted, and if one candidate
#receives more than 50% of the vote then that candidate is elected. However, if
#no candidate receives more than 50%, all candidates tied for the lowest number
#of votes are eliminated. Ballots ranking these candidates first are recounted
#in favor of their highest-ranked non-eliminated candidate. This process of
#eliminating the weakest candidates and counting their ballots in favor of the
#preferred non-eliminated candidate continues until one candidate
#receives more than 50% of the vote, or until all remaining candidates are tied.



import sys

names=[]

def main():
        #get the number of elections
        num_elections= input()
        print(num_elections +"\n")
        num_elections= int(num_elections)
        with open(file, "r") as f:
                for line in f:
                        names.append(line.rstrip())
        while num_elections>0:
                #get the number of candidatwes for that election
                numcandidates= input()
                candidates=[0]*int(numcandidates)
                #randomly generate a set of candidates
                s= Set()
                while len(s)<int(numcandidates):
                        s.add(random.randint(1, len(names))
                count=0
                for i in s:
                        candidates[count]=names[i-1]
                        count+=1
                #generate the ballot results
                w=input()
                candidateweights=int(w)*int(numcandidates)
                ballots=[]
                while(candidateweights > 0):
                        s=Set()
                        while len(s)<int(numcandidates):
                                s.add(random.randint(1, numcandidates)      
                        s=random.sample(s, len(s))
                        ballots.append(s)
                        candidateweights-=1

                maxvotes=evaluate(ballots,candidates)
                getwinner(maxvotes,ballots, candidates)

def evaluate (ballots,candidates):
		'''
		Determines the winner of the election.
		'''
                maxvotes=[]                      
		for ballot in ballots:
			topvote = ballot.split('\n')[1]
			topcandidate = candidates[topvote]
			maxvotes.add(topcandidate)
                return maxvotes
                        
def getwinner(maxvotes, ballots, candidates)
                '''
		Determines the winner of the election.
		'''
		while (True):
			# Check for a clear winner
			majority = len(maxvotes) / 2
                        votes =winners=leastVotes= []
			for maxvote in maxvotes:
                                if maxvotes.count(maxvote) > majority:
                                        return maxvote
                                        break
                                else:
                                        votes.append(maxvotes.count(maxvote))# Here, votes counts the number of times the candidate appears in the ballot winners list

                        sortedvotes=sorted(votes, key=int,  reverse=True)
                        if len(sortedvotes) > 0:
                               # Check for an all-way tie
                                        winners.append(s for sortedvotes in s if s=sortedvotes[0] )
                                        return winners
                                        break


			# Find the least number of votes
			leastVotes.append(s for sortedvotes in s if s=sortedvotes[-1] )

			# Remove all candidates with the least number of votes
			for maxvote in maxvotes:
				if leastVotes == maxvotes.count(maxvote):
                                        removed.append(maxvote)

                        return(getwinner(replace(removed, maxvotes, ballots, candidates), ballots, candidates))
        
def replace(removed, maxvotes, ballots, candidates):
                        
                        newmaxvotes=[]
			# Redistribute ballots from removed candidate
                        for ballot in ballots:
                                      total=len(ballot.split('\n'))
                                      if candidates[ballot.split('\n')[1]]in removed:
                                              for i in range(2,total):
                                                        if candidates[ballot.split('\n')[i]] not in removed:
                                                                       newmaxvotes.add(candidates[candidates[ballot.split('\n')[i]])
                                                                       break
                                                        else:
                                                                       i+=1
                                        
                                        else:
                                                newmaxvotes.append(candidates[ballot.split('\n')[1]])
                        return newmaxvotes
			                         
                                
                                      
