donation = {
    'ali' : 200,
    'zara': 5010,
    'mahdi': 100,
    'hasan': 1200
}

def donation_analysis(d):
    total = sum(d.values())
    average = total / len(d.values())
    maximum = list(d.keys())[list(d.values()).index(max(d.values()))]
    return total, average, maximum

total, ave, most = donation_analysis(donation)
print(f"total donation = {total} and average = {ave} and most donation belong to {most}")