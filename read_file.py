class ReadFile:
    def readFile():
        output = ["","","","","","","","","",""];
        # print("Reading the file");
        count = 0;
        with open('conversion.txt', 'r') as f:
            for line in f:
                output[count] = line.strip();
                count += 1
               # print(line.strip());


            f.close();
        return output;

