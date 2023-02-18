import json


def branch_coverage_parser():
    """
        Reads from data/branch-coverage file, parses its content and prints out as a JSON object
    """
    data = {}

    with open("data/branch-coverage", "r") as f:
        content = f.readlines()

    # Remove title and column names from content
    content = content[2:]

    for line in content:
        # Seperate column values into variables
        func_name, total_branches, ratio, branches_not_found = line.split(",")
        total_branches = int(total_branches)
        ratio = float(ratio)
        # Convert branches_not_found into a set of integers
        branches_not_found = set(map(int, branches_not_found.split(";")))
        if func_name not in data:
            data[func_name] = {
                "total_branches": total_branches,
                "ratio": ratio,
                "branches_not_found": branches_not_found
            }
        else:
            if data[func_name]["branches_not_found"] == set([0]):
                    # Tests cover all branches
                    continue
            intersect = data[func_name]["branches_not_found"].intersection(branches_not_found)
            if len(intersect) == 0:
                data[func_name]["branches_not_found"] = set([0])
                data[func_name]["ratio"] = 1.0
            else:
                data[func_name]["branches_not_found"] = intersect
                data[func_name]["ratio"] = (total_branches - len(intersect)) / total_branches

    # Change branches_not_found to a list so it becomes JSON serializable
    for key in data.keys():
        data[key]["branches_not_found"] = list(data[key]["branches_not_found"])
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == "__main__":
    branch_coverage_parser()