def best_set(votes):
    maxVotes = {}
    for artist in votes.values():
        if artist in maxVotes:
            maxVotes[artist] += 1
        else:
            maxVotes[artist] = 1

    # maxNum = -1
    # maxNames = ""
    # for name in maxVotes.keys():
    #     if maxVotes[name] > maxNum:
    #         maxNum = maxVotes[name]
    #         maxNames = name

    # maxV = maxVotes.get(max(maxVotes.values()))

    return max(maxVotes, key = maxVotes.get)


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))