def cycle_crossover(parent1, parent2):
    output = []
    cycles = []

    def pre_output():
        cycles_index = []
        for i in parent1:
            for x in range(len(cycles)):
                take = False
                for y in cycles[x]:
                    if y==i:
                        cycles_index.append(x+1)
                        take = True
                        break
                if take==True:
                    break
        for i in range(len(cycles_index)):
            if cycles_index[i]%2==0:
                output.append(parent2[i])
            else:
                output.append(parent1[i])
        return output

    def search_parent1(value):
        if(value == initial):
            return
        for i in range(0, len(parent1) + 1):
            if(parent1[i]==value):
                cycle.append(value)
                search_parent2(i)
                return

    def search_parent2(position):
        search_parent1(parent2[position])
        return

    for i in range(len(parent1)):
        cycle = []
        initial = parent1[i]
        cycle.append(parent1[i])
        search_parent2(i)
        cycles.append(cycle)

    return pre_output()