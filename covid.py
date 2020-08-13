from tkinter import *
root = Tk()
root.geometry("400x400")
root.title("Get Covid-19 data country wise")




def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    root.update()
    countries = data.get()
    country_name = countries.strip()
    country_name = country_name.replace(" ", ",")
    country_name = country_name.split(",")
    for x in country_name:
        cases.append(covid.get_status_by_country_name(x))
        root.update()
    for y in cases:
        confirmed.append(y["confirmed"])
        active.append(y["active"])
        deaths.append(y["deaths"])
        recovered.append(y["recovered"])
    confirmed_patch = mpatches.Patch(color='green', label='confirmed')  
    recovered_patch = mpatches.Patch(color='red', label='recovered')
    active_patch = mpatches.Patch(color='blue', label='active')
    deaths_patch = mpatches.Patch(color='black', label='deaths')
    plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])
    for x in range(len(country_name)):
        plt.bar(country_name[x], confirmed[x], color='green')
        if recovered[x] > active[x]:
            plt.bar(country_name[x], recovered[x], color='red')
            plt.bar(country_name[x], recovered[x], color='blue')
        else:
            plt.bar(country_name[x], active[x], color='blue')
            plt.bar(country_name[x], recovered[x], color='red')
      
        plt.bar(country_name[x], deaths[x], color='red')
    plt.title('Current Covid Cases')
    plt.xlabel('Country name')
    plt.ylabel('cases in millions')
    plt.show()


  
    
    
    
    
    
    
    
    
    
    
    
    
Label(root, text="Enter all countries names\nfor whom want ro get Covid-19 data").pack()
Label(root, text="Enter country name").pack()
data = StringVar()
data.set("separate country names by space or comma") 
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Get Data", command=showdata).pack()
root.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    