import os
def find_files(filename, path):
    result = []
    for root, dir, files in os.walk(path):
        for file in files:
            if file.endswith(filename):
                result.append(os.path.join(root, file))
    return result
    
if __name__ == "__main__":
    print(find_files('.txt', 'path'))
