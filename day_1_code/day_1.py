

def read_text_file(filename):
    '''Reads in text file of numbers, returns number in list'''
    with open(filename,'r') as file1:
        lines = file1.readlines()
        list_of_numbers = []
        for line in lines:
            list_of_numbers.append(int(line))
    return(list_of_numbers)


def sum_to_2020(numbers):
    '''Compares numbers in list to find a pair that sum to 2020'''
    counter=0
    while counter < len(numbers):
        for i in range(counter,len(numbers)):
            s = numbers[counter] + numbers[i]
            # if 2020 leave the for loop. 
            if s == 2020:
                break
        else:
            counter = counter+1
            continue
        break
    fin_list = [numbers[counter], numbers[i]]
    return(fin_list)


def sum_to_2020_3(numbers):
    '''Compares numbers in list to find a 3 numbers that sum to 2020'''
    counter=0
    while counter < len(numbers):
        for i in range(counter,len(numbers)):
            if i == counter:
                continue
            a=numbers[counter]
            b=numbers[i]
            for t in range(i,len(numbers)):
                if t == i:
                    continue
                c=numbers[t]
                s = numbers[counter] + numbers[i] + numbers[t]
            # if 2020 leave the for loop. 
                if s == 2020:
                    break
            else:
                continue
            break
        else:
            counter = counter+1
            continue
        break
    fin_list = [numbers[counter], numbers[i],numbers[t]]
    return(fin_list)


if __name__ == '__main__':
    # read in file 
    numbers1 = read_text_file('day_1_code/day_1_input.txt')
    # print(len(numbers1))
  
    # calculate the pair whihc sum to 2020 
    answer_list = sum_to_2020_3(numbers1)
    print(answer_list)
    # print 2 numbers multiplied
    print(answer_list[0]*answer_list[1]*answer_list[2])
