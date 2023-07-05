import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Person:
    def __init__(self):
        self.wealth = [1024]
        self.ability = int(np.random.normal(50, 10))
        if self.ability < 0:
            self.ability = 0
        if self.ability > 100:
            self.ability = 100

    def event(self):
        prob = np.random.randint(0, 10)
        if prob < 2:
            self.wealth.append(self.wealth[-1] * 0.5+2048)
        elif prob > 6:
            ab_prob = np.random.randint(0, 101)
            if ab_prob < self.ability:
                self.wealth.append(self.wealth[-1] * 2+2048)
            else:
                self.wealth.append(self.wealth[-1]+2048)
        else:
            self.wealth.append(self.wealth[-1]+1024)


def simulate():
    people = []
    for i in range(1000):
        person = Person()
        for ii in range(100):
            person.event()

        people.append(person)
    return people

def result_in_df():
    columns = ["ability", "W20"]
    for i in range(100):
        string = "W"
        age = 20 + (i + 1) / 2
        string = string + str(age)
        columns.append(string)

    df_result = pd.DataFrame(columns=columns)
    for i in range(len(people)):
        df_result.loc[i, "ability"] = people[i].ability
        for ii in range(len(columns)):
            if ii == 0:
                pass
            else:
                df_result.loc[i, columns[ii]] = people[i].wealth[ii - 1]


    return df_result

if __name__ == "__main__":

    people = simulate()

    df_result = result_in_df()

    df_result.to_csv("df_result.csv")
    ###########################################

    Final_wealth = df_result["W70.0"]
    ability = df_result["ability"]
    age = df_result.columns[1:]

    ###########################################


    plt.scatter(ability, Final_wealth)
    plt.xlabel('Ability')
    plt.ylabel('Wealth')
    plt.title('Ability vs Wealth')
    plt.savefig('Ability_Wealth.png')
    plt.show()



    plt.hist(ability, bins=10, edgecolor='black')
    plt.xlabel('Ability')
    plt.ylabel('Frequency')
    plt.title('Ability Distribution')
    plt.savefig('Ability_Distribution.png')

    plt.show()
    ##################
    # Show Max history
    maxIndex = 0
    maxW = 0
    for i in range(df_result.shape[0]):
        if df_result.loc[i, "W70.0"] > maxW:
            maxW = df_result.loc[i, "W70.0"]
            maxIndex = i

    print("Max wealth:")
    print(maxW)
    print("Ability of this person:")
    print(df_result.loc[maxIndex, "ability"])
    wealths = df_result.drop('ability', axis=1).iloc[maxIndex]
    Max_wealths = df_result.drop('ability', axis=1).loc[maxIndex, "W70.0"]

    plt.plot(age, wealths)
    plt.xlabel('Age')
    plt.ylabel('Wealth')
    plt.title('Age vs Wealth')
    plt.savefig('Max_person.png')
    plt.show()

    # Show Min history
    minIndex = 0
    minW = 0
    for i in range(df_result.shape[0]):
        if i == 0:
            minIndex = i
            minW = df_result.loc[i, "W70.0"]
        if df_result.loc[i, "W70.0"] < minW:
            minW = df_result.loc[i, "W70.0"]
            minIndex = i
    print("Min wealth:")
    print(minW)
    print("Ability of this person:")
    print(df_result.loc[minIndex, "ability"])
    wealths = df_result.drop('ability', axis=1).iloc[minIndex]

    plt.plot(age, wealths)
    plt.xlabel('Age')
    plt.ylabel('Wealth')
    plt.title('Age vs Wealth')
    plt.savefig('Min_person.png')
    plt.show()



    # If Pareto principle
    print("Mean")
    print(df_result["W70.0"].mean())
    print("Mode")
    print(df_result["W70.0"].mode())
    print("Median")
    print(df_result["W70.0"].median())
    print("Sum")
    sum70 = float(df_result["W70.0"].sum())
    print(df_result["W70.0"].sum())
    print("max/sum:")
    print(Max_wealths / sum70)

    sorted_W70 = df_result.sort_values(by=["W70.0"], ascending=False)["W70.0"]

    sum_20 = 0
    for i in range(int(0.2 * sorted_W70.shape[0])):
        sum_20 += sorted_W70.iloc[i]

    print("max20/sum:")
    print(sum_20 / sum70)
