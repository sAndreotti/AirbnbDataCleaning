import json

cleanml = json.load(open("./clean_data/CleanML/dirty_10_result.json"))

best = []
for item in cleanml:
    if best == []:
        best = item

    if cleanml[item]['train_acc'] > cleanml[best]['train_acc']:
        best = item

print(best)
print(json.dumps(cleanml[best], indent = 4, sort_keys=True))