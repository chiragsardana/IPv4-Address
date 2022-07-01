class SaveToFile:
    def saveToFile(output : list):
        with open('conversion.txt', 'w') as f:
            for line in output:
                f.write(line)
                f.write('\n')
            f.close();